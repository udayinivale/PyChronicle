import sys
import os
import time
import json
import copy
from typing import Dict, Any, Tuple, List, Optional
from . import db

class PyChronicleTracer:
    def serialize_value(self, val: Any) -> Tuple[str, str]:
        val_type = type(val).__name__
        try:
            if isinstance(val, (int, float, str, bool, type(None))):
                return json.dumps(val), val_type
            elif isinstance(val, (list, dict, tuple, set)):
                serialized = json.dumps(self._make_serializable(val))
                if len(serialized) > 5000:
                    return serialized[:5000] + "... [truncated]", val_type
                return serialized, val_type
            else:
                return repr(val), val_type
        except Exception as e:
            return f"<Unserializable {val_type}: {str(e)}>", val_type

    def _make_serializable(self, obj: Any) -> Any:
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, dict):
            return {str(k): self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self._make_serializable(x) for x in obj]
        elif isinstance(obj, set):
            return [self._make_serializable(x) for x in list(obj)]
        else:
            return repr(obj)

    def __init__(self, script_path: str, db_path: str):
        self.script_path = os.path.abspath(script_path)
        self.db_path = db_path
        self.run_id = None
        self.step_number = 0
        self.frame_locals_cache: Dict[int, Dict[str, Any]] = {}
        db.init_db(self.db_path)

    def trace_execution(self):
        self.run_id = db.create_run(self.db_path, self.script_path)
        self.step_number = 0
        self.frame_locals_cache: Dict[int, Dict[str, Any]] = {}

        with open(self.script_path, "r", encoding="utf-8") as f:
            source = f.read()
        compiled_code = compile(source, self.script_path, "exec")
        
        globals_dict = {
            "__file__": self.script_path,
            "__name__": "__main__",
            "__builtins__": __builtins__,
        }
        locals_dict = globals_dict

        def global_trace(frame, event, arg):
            if os.path.abspath(frame.f_code.co_filename) == self.script_path:
                return local_trace
            return None

        def local_trace(frame, event, arg):
            if os.path.abspath(frame.f_code.co_filename) != self.script_path:
                return None

            if event in ("line", "call", "return"):
                self.step_number += 1
                line_number = frame.f_lineno
                func_name = frame.f_code.co_name
                timestamp = time.time()

                step_id = db.insert_step(
                    self.db_path,
                    self.run_id,
                    self.step_number,
                    line_number,
                    func_name,
                    event,
                    timestamp
                )
                
                frame_id = id(frame)
                current_locals = {}
                for k, v in frame.f_locals.items():
                    if k.startswith("__") or k == "sys" or k == "os" or k == "_pychronicle_trace_locals":
                        continue
                    current_locals[k] = v

                prev_locals = self.frame_locals_cache.get(frame_id, {})
                deltas = []
                for k, v in current_locals.items():
                    serialized_val, val_type = self.serialize_value(v)
                    is_changed = False
                    if k not in prev_locals:
                        is_changed = True
                    else:
                        prev_serialized, _ = self.serialize_value(prev_locals[k])
                        if prev_serialized != serialized_val:
                            is_changed = True
                    if is_changed:
                        deltas.append((k, val_type, serialized_val))

                for k in prev_locals:
                    if k not in current_locals:
                        deltas.append((k, "NoneType", "None [deleted]"))

                if deltas:
                    db.insert_variable_states(self.db_path, step_id, deltas)

                cached_locals = {}
                for k, v in current_locals.items():
                    try:
                        cached_locals[k] = copy.deepcopy(v)
                    except Exception:
                        cached_locals[k] = copy.copy(v)
                self.frame_locals_cache[frame_id] = cached_locals

                if event == "return" and frame_id in self.frame_locals_cache:
                    del self.frame_locals_cache[frame_id]
            return local_trace

        original_trace = sys.gettrace()
        sys.settrace(global_trace)
        try:
            exec(compiled_code, globals_dict, locals_dict)
        finally:
            sys.settrace(original_trace)

import sys
import os
import time
import json
import copy
from typing import Dict, Any, Tuple, List, Optional
from . import db

class PyChronicleTracer:
    def __init__(self, script_path: str, db_path: str):
        self.script_path = os.path.abspath(script_path)
        self.db_path = db_path
        self.run_id = None
        self.step_number = 0
        db.init_db(self.db_path)

    def trace_execution(self):
        self.run_id = db.create_run(self.db_path, self.script_path)
        self.step_number = 0

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
            return local_trace

        original_trace = sys.gettrace()
        sys.settrace(global_trace)
        try:
            exec(compiled_code, globals_dict, locals_dict)
        finally:
            sys.settrace(original_trace)

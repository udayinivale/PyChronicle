import os
import sys
import json

from . import db


class PyChronicleTracer:

    def __init__(self, script_path, db_path):
        self.script_path = os.path.abspath(script_path)
        self.db_path = db_path
        self.run_id = None
        self.step_number = 0

        db.init_db(self.db_path)

    def _make_serializable(self, obj):

        if isinstance(obj, (int, float, str, bool)):
            return obj

        if obj is None:
            return None

        if isinstance(obj, list):
            return [self._make_serializable(x) for x in obj]

        if isinstance(obj, tuple):
            return [self._make_serializable(x) for x in obj]

        if isinstance(obj, dict):
            return {
                str(k): self._make_serializable(v)
                for k, v in obj.items()
            }

        if isinstance(obj, set):
            return [
                self._make_serializable(x)
                for x in obj
            ]

        return repr(obj)

    def serialize_value(self, value):

        try:
            return json.dumps(
                self._make_serializable(value)
            )
        except Exception:
            return repr(value)

    def trace_execution(self):

        self.run_id = db.create_run(
            self.db_path,
            self.script_path
        )

        self.step_number = 0

        with open(
            self.script_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()

        code = compile(
            source,
            self.script_path,
            "exec"
        )

        def trace(frame, event, arg):

            if event != "line":
                return trace

            filename = os.path.abspath(
                frame.f_code.co_filename
            )

            if filename != self.script_path:
                return trace

            self.step_number += 1

            db.insert_step(
                self.db_path,
                self.run_id,
                self.step_number,
                frame.f_lineno,
                frame.f_code.co_name,
                event
            )

            variables = {}

            for name, value in frame.f_locals.items():

                if name.startswith("__"):
                    continue

                variables[name] = self.serialize_value(value)

            db.insert_variables(
                self.db_path,
                self.run_id,
                self.step_number,
                variables
            )

            return trace

        globals_dict = {
            "__name__": "__main__",
            "__file__": self.script_path,
            "__builtins__": __builtins__,
        }

        sys.settrace(trace)

        try:
            exec(code, globals_dict, globals_dict)
        finally:
            sys.settrace(None)
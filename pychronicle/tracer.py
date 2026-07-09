import sys
import os
import time
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

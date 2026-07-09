import os
from typing import Dict, Any, List
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class PyChronicleApp(App):
    def __init__(self, db_path: str, run_id: int, script_path: str):
        super().__init__()
        self.db_path = db_path
        self.run_id = run_id
        self.script_path = os.path.abspath(script_path)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

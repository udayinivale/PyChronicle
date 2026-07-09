import os
from typing import Dict, Any, List
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, DataTable, Label, Slider
from textual.binding import Binding

class PyChronicleApp(App):
    CSS = """
    Screen {
        background: $background;
    }
    #main-layout {
        layout: grid;
        grid-size: 2;
        grid-columns: 3fr 2fr;
        height: 1fr;
        margin: 0 1;
    }
    #code-container {
        border: solid $primary-background-lighten-2;
        border-title-color: $accent;
        height: 1fr;
        overflow: scroll scroll;
        background: $boost;
    }
    #vars-container {
        border: solid $primary-background-lighten-2;
        border-title-color: $accent;
        height: 1fr;
        background: $boost;
    }
    #timeline-container {
        height: auto;
        border: solid $primary-background-lighten-2;
        border-title-color: $accent;
        margin: 1 1 0 1;
        padding: 0 1;
        layout: horizontal;
        align: center middle;
        background: $boost;
    }
    #step-label {
        width: 15%;
        text-align: center;
        content-align: center middle;
        text-style: bold;
        color: $accent;
    }
    #timeline-slider {
        width: 70%;
    }
    #info-label {
        width: 15%;
        text-align: right;
        content-align: right middle;
        color: $text-muted;
    }
    """

    BINDINGS = [
        Binding("left,h", "step_backward", "Step Back", show=True),
        Binding("right,l", "step_forward", "Step Forward", show=True),
        Binding("up,k", "first_step", "First Step", show=True),
        Binding("down,j", "last_step", "Last Step", show=True),
        Binding("q", "quit", "Quit", show=True),
    ]

    def __init__(self, db_path: str, run_id: int, script_path: str):
        super().__init__()
        self.db_path = db_path
        self.run_id = run_id
        self.script_path = os.path.abspath(script_path)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="main-layout"):
            with Container(id="code-container") as c:
                c.border_title = f"Source Code - {os.path.basename(self.script_path)}"
                yield Static(id="code-view", expand=True)
            with Container(id="vars-container") as v:
                v.border_title = "Variable Inspector (f_locals)"
                yield DataTable(id="vars-table")
        yield Footer()

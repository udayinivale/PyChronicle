from . import db
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
        layout: vertical;
    }
    #vars-table {
        height: 60%;
    }
    #history-container {
        border-top: solid $primary-background-lighten-2;
        height: 40%;
        overflow: scroll scroll;
        background: $boost;
    }
    #history-view {
        padding: 0 1;
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

    def __init__(self, db_path: str, run_id: int, script_path: str):
        super().__init__()
        self.db_path = db_path
        self.run_id = run_id
        self.script_path = os.path.abspath(script_path)
        
        with open(self.script_path, "r", encoding="utf-8") as f:
            self.source_code = f.read()
            
        self.steps = db.get_run_steps(self.db_path, self.run_id)
        self.total_steps = len(self.steps)
        self.current_step_idx = 0

        try:
            from . import ast_analyzer
            analysis = ast_analyzer.analyze_script(self.script_path)
            self.static_vars = analysis["assigned_variables"]
        except Exception:
            self.static_vars = []

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="main-layout"):
            with Container(id="code-container") as c:
                c.border_title = f"Source Code - {os.path.basename(self.script_path)}"
                yield Static(id="code-view", expand=True)
            with Container(id="vars-container") as v:
                v.border_title = "Variable Inspector (f_locals)"
                yield DataTable(id="vars-table")
                with Container(id="history-container") as hc:
                    hc.border_title = "Variable History Timeline"
                    yield Static("Select a variable above to view its mutation history.", id="history-view")
        with Horizontal(id="timeline-container") as t:
            t.border_title = "Execution Scrubber"
            yield Label("Step 0 / 0", id="step-label")
            if self.total_steps > 1:
                yield Slider(min=1, max=self.total_steps, value=1, id="timeline-slider")
            else:
                yield Label("[No execution steps recorded]", id="timeline-slider")
            yield Label("Line: --", id="info-label")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#vars-table", DataTable)
        table.cursor_type = "row"
        table.add_columns("Variable", "Type", "Value")
        self.update_step_ui()

    def update_step_ui(self) -> None:
        if not self.steps:
            self.query_one("#code-view", Static).update("No steps to display.")
            return

        step = self.steps[self.current_step_idx]
        step_number = step["step_number"]
        line_number = step["line_number"]
        event = step["event"]
        func_name = step["function_name"]

        self.query_one("#step-label", Label).update(f"Step {step_number} / {self.total_steps}")
        self.query_one("#info-label", Label).update(f"Line {line_number} ({event})")
        
        code_container = self.query_one("#code-container")
        code_container.border_title = f"Source Code - {os.path.basename(self.script_path)} [in {func_name}()]"

        try:
            slider = self.query_one("#timeline-slider", Slider)
            if slider.value != step_number:
                slider.value = step_number
        except Exception:
            pass

        from rich.syntax import Syntax
        syntax = Syntax(self.source_code, "python", theme="monokai", line_numbers=True, highlight_lines={line_number})
        self.query_one("#code-view", Static).update(syntax)
        
        code_container.scroll_to(y=max(0, line_number - 10), animate=False)
        self.populate_variables(step["step_id"])

    def populate_variables(self, step_id: int) -> None:
        table = self.query_one("#vars-table", DataTable)
        table.clear()
        
        var_states = db.get_variable_states_at_step(self.db_path, step_id)
        display_vars = {}
        for var in self.static_vars:
            display_vars[var] = {"type": "N/A", "value": "<undefined>"}
        for var_name, var_info in var_states.items():
            display_vars[var_name] = var_info
            
        for var_name, var_info in sorted(display_vars.items()):
            table.add_row(var_name, var_info["type"], var_info["value"])

    def on_slider_changed(self, event: Slider.Changed) -> None:
        step_val = int(event.value)
        idx = step_val - 1
        if 0 <= idx < self.total_steps and idx != self.current_step_idx:
            self.current_step_idx = idx
            self.update_step_ui()

    def action_step_forward(self) -> None:
        if self.current_step_idx < self.total_steps - 1:
            self.current_step_idx += 1
            self.update_step_ui()

    def action_step_backward(self) -> None:
        if self.current_step_idx > 0:
            self.current_step_idx -= 1
            self.update_step_ui()

    def action_first_step(self) -> None:
        if self.total_steps > 0:
            self.current_step_idx = 0
            self.update_step_ui()

    def action_last_step(self) -> None:
        if self.total_steps > 0:
            self.current_step_idx = self.total_steps - 1
            self.update_step_ui()

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        try:
            row_values = event.data_table.get_row(event.row_key)
            var_name = row_values[0]
            
            history = db.get_variable_history(self.db_path, self.run_id, var_name)
            
            from rich.text import Text
            
            text = Text()
            text.append(f"History of '{var_name}':\n", style="bold yellow")
            
            if not history:
                text.append("No mutations recorded (variable is undefined or static).", style="italic red")
            else:
                for h in history:
                    text.append(f"\n• Step {h['step_number']} (Line {h['line_number']}): ", style="cyan")
                    text.append(f"{h['serialized_value']}", style="green")
                    text.append(f" [type: {h['variable_type']}]", style="dim text-muted")
                    
            self.query_one("#history-view", Static).update(text)
        except Exception as e:
            self.query_one("#history-view", Static).update(f"Error loading history: {e}")

import os
import sys
import click
import sqlite3
from .tracer import PyChronicleTracer
from .tui import PyChronicleApp
from . import db

def get_latest_run_info(db_path: str) -> click.Tuple:
    if not os.path.exists(db_path):
        raise click.ClickException(f"Database file not found: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT run_id, script_path FROM runs ORDER BY run_id DESC LIMIT 1").fetchone()
        if not row:
            raise click.ClickException(f"No runs found in database: {db_path}")
        return row["run_id"], row["script_path"]
    except Exception as e:
        raise click.ClickException(f"Failed to query database: {e}")
    finally:
        conn.close()

@click.group()
def main():
    """PyChronicle: AST-Powered Time-Travel Debugger for Python."""
    pass

@main.command()
@click.argument("script_path", type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option("--db-path", default="pychronicle_trace.db", help="Path to SQLite trace database.")
def run(script_path: str, db_path: str):
    """Trace the execution of a Python script and inspect it in the TUI."""
    click.echo(f"[*] Initializing tracer for: {script_path}")
    click.echo(f"[*] SQLite database: {db_path}")

    tracer = PyChronicleTracer(script_path, db_path)
    click.echo("[*] Executing and tracing script execution...")
    try:
        tracer.trace_execution()
    except Exception as e:
        click.echo(f"[!] Target script crashed: {e}", err=True)
    
    click.echo(f"[+] Trace completed. Recorded {tracer.step_number} execution steps.")
    click.echo("[*] Launching time-travel debugging Terminal UI...")
    
    app = PyChronicleApp(db_path, tracer.run_id, script_path)
    app.run()

@main.command()
@click.argument("db_path", type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option("--run-id", type=int, default=None, help="Specific run ID to view (defaults to latest run).")
def view(db_path: str, run_id: int):
    """Launch the TUI to view a pre-recorded execution trace."""
    if run_id is None:
        run_id, script_path = get_latest_run_info(db_path)
    else:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT script_path FROM runs WHERE run_id = ?", (run_id,)).fetchone()
        conn.close()
        if not row:
            raise click.ClickException(f"Run ID {run_id} not found in database: {db_path}")
        script_path = row["script_path"]

    if not os.path.exists(script_path):
        raise click.ClickException(f"Original script file is missing: {script_path}")

    click.echo(f"[*] Loading run {run_id} for script: {script_path}")
    app = PyChronicleApp(db_path, run_id, script_path)
    app.run()

if __name__ == "__main__":
    main()

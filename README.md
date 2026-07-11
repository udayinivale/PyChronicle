# PyChronicle

PyChronicle is an AST-powered time-travel debugger for Python. It records script execution into an SQLite trace database and lets you inspect the execution flow with a terminal-based UI.

## Requirements

- Python 3.8+
- `click`
- `rich`
- `textual`

Install dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Usage

From the project root (`c:\Users\victus\Desktop\PyChronicle\pychronicle`):

Trace a script and start the debugger UI:

```powershell
python -m pychronicle.cli run example.py
```

This creates or updates `pychronicle_trace.db` by default.

View a previously recorded trace:

```powershell
python -m pychronicle.cli view pychronicle_trace.db
```

To view a specific run if the database contains more than one:

```powershell
python -m pychronicle.cli view pychronicle_trace.db --run-id 1
```

## Notes

- Ensure you run commands from the repository root where `requirements.txt` is located.
- If you see `Could not open requirements file`, it means the command was run from the wrong directory or the filename was misspelled.

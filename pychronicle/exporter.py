import json
from pychronicle.viewer import (
    get_run_details,
    get_execution_steps,
    get_all_variables
)


def export_to_json(db_path, run_id, output_file):
    run = get_run_details(db_path, run_id)
    steps = get_execution_steps(db_path, run_id)
    variables = get_all_variables(db_path, run_id)

    data = {
        "run": {
            "run_id": run[0],
            "script_path": run[1],
            "started_at": run[2]
        },
        "steps": [],
        "variables": []
    }

    for step in steps:
        data["steps"].append({
            "step_number": step[0],
            "line_number": step[1]
        })

    for variable in variables:
        data["variables"].append({
            "step_number": variable[0],
            "name": variable[1],
            "value": variable[2]
        })

    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

    print("Export Successful")
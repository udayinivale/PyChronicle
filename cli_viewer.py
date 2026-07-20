from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

DB = "pychronicle.db"

print("=" * 40)
print("        PYCHRONICLE VIEWER")
print("=" * 40)

runs = get_runs(DB)

print("\nAvailable Runs\n")

for run in runs:
    print(
        f"Run ID : {run[0]}"
    )
    print(
        f"Script : {run[1]}"
    )
    print(
        f"Time   : {run[2]}"
    )
    print("-" * 40)

run_id = int(input("\nEnter Run ID: "))

steps = get_execution_steps(DB, run_id)

print("\nExecution Steps\n")

for step in steps:
    print(
        f"Step {step[0]}  ->  Line {step[1]}"
    )

step_number = int(
    input("\nEnter Step Number: ")
)

variables = get_variables(
    DB,
    run_id,
    step_number
)

print("\nVariables\n")

for name, value in variables:
    print(f"{name} = {value}")
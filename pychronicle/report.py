from pychronicle.viewer import (
    get_run_details,
    get_execution_steps,
    get_all_variables
)


def generate_report(db_path, run_id):
    run = get_run_details(db_path, run_id)
    steps = get_execution_steps(db_path, run_id)
    variables = get_all_variables(db_path, run_id)

    print("=" * 50)
    print("PYCHRONICLE TRACE REPORT")
    print("=" * 50)

    print(f"Run ID      : {run[0]}")
    print(f"Script Path : {run[1]}")
    print(f"Started At  : {run[2]}")

    print("\nExecution Steps")
    print("-" * 50)

    for step in steps:
        print(f"Step {step[0]} -> Line {step[1]}")

    print("\nVariables")
    print("-" * 50)

    for variable in variables:
        print(
            f"Step {variable[0]} : "
            f"{variable[1]} = {variable[2]}"
        )
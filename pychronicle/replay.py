import time

from pychronicle.viewer import (
    get_execution_steps,
    get_variables
)


def replay_trace(db_path, run_id, delay=1):
    steps = get_execution_steps(db_path, run_id)

    print("\n===== TRACE REPLAY =====\n")

    for step_number, line_number in steps:

        print(f"Step {step_number}")
        print(f"Executing Line : {line_number}")

        variables = get_variables(
            db_path,
            run_id,
            step_number
        )

        if variables:
            print("Variables")

            for name, value in variables:
                print(f"  {name} = {value}")

        else:
            print("No Variables")

        print("-" * 40)

        time.sleep(delay)
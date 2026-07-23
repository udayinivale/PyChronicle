from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

from pychronicle.exporter import export_to_json

DB = "pychronicle.db"


while True:

    print("\n========== PYCHRONICLE ==========")
    print("1. View Runs")
    print("2. Export Run")
    print("3. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        runs = get_runs(DB)

        print("\nRuns")

        for run in runs:
            print(run)

        run_id = int(input("\nRun ID: "))

        steps = get_execution_steps(DB, run_id)

        print("\nSteps")

        for step in steps:
            print(step)

        step_number = int(input("\nStep Number: "))

        variables = get_variables(
            DB,
            run_id,
            step_number
        )

        print("\nVariables")

        for name, value in variables:
            print(name, "=", value)

    elif choice == "2":

        run_id = int(input("Run ID: "))

        export_to_json(
            DB,
            run_id,
            "trace.json"
        )

    elif choice == "3":

        print("Goodbye")
        break

    else:

        print("Invalid Choice")

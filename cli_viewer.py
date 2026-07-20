from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

DB = "pychronicle.db"


def show_runs():
    runs = get_runs(DB)

    print("\nAvailable Runs\n")

    for run in runs:
        print(f"Run ID : {run[0]}")
        print(f"Script : {run[1]}")
        print(f"Time   : {run[2]}")
        print("-" * 40)


def show_steps(run_id):
    steps = get_execution_steps(DB, run_id)

    print("\nExecution Steps\n")

    for step in steps:
        print(f"Step {step[0]} -> Line {step[1]}")


def show_variables(run_id, step):
    variables = get_variables(DB, run_id, step)

    print("\nVariables\n")

    if not variables:
        print("No variables found.")
        return

    for name, value in variables:
        print(f"{name} = {value}")


while True:

    print("\n========== PYCHRONICLE ==========")
    print("1. View Runs")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        show_runs()

        run_id = int(input("\nEnter Run ID: "))

        show_steps(run_id)

        step = int(input("\nEnter Step Number: "))

        show_variables(run_id, step)

    elif choice == "2":

        print("Goodbye!")
        break

    else:

        print("Invalid Choice")
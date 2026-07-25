from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

from pychronicle.exporter import export_to_json
from pychronicle.replay import replay_trace

DB = "pychronicle.db"


def show_runs():

    runs = get_runs(DB)

    print("\nAvailable Runs\n")

    for run in runs:
        print(f"Run ID : {run[0]}")
        print(f"Script : {run[1]}")
        print(f"Time   : {run[2]}")
        print("-" * 40)


while True:

    print("\n========== PYCHRONICLE ==========")
    print("1. View Runs")
    print("2. Replay Run")
    print("3. Export Run")
    print("4. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        show_runs()

    elif choice == "2":

        run_id = int(input("Run ID : "))

        replay_trace(
            DB,
            run_id
        )

    elif choice == "3":

        run_id = int(input("Run ID : "))

        export_to_json(
            DB,
            run_id,
            "trace.json"
        )

    elif choice == "4":

        print("Goodbye")
        break

    else:

        print("Invalid Choice")
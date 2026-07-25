from pychronicle.ui import (
    show_title,
    show_menu,
    show_message
)

from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

from pychronicle.replay import replay_trace
from pychronicle.exporter import export_to_json
from pychronicle.search import search_variable

DB = "pychronicle.db"


while True:

    show_title()
    show_menu()

    choice = input("\nEnter Choice: ")

    # -------------------------------
    # View Runs
    # -------------------------------
    if choice == "1":

        runs = get_runs(DB)

        if not runs:
            show_message("No execution runs found.", "red")
            continue

        print("\n========== AVAILABLE RUNS ==========\n")

        for run in runs:
            print(f"Run ID : {run[0]}")
            print(f"Script : {run[1]}")
            print(f"Time   : {run[2]}")
            print("-" * 40)

        run_id = int(input("\nEnter Run ID: "))

        steps = get_execution_steps(DB, run_id)

        if not steps:
            show_message("No execution steps found.", "red")
            continue

        print("\n========== EXECUTION STEPS ==========\n")

        for step in steps:
            print(f"Step {step[0]} -> Line {step[1]}")

        step_number = int(input("\nEnter Step Number: "))

        variables = get_variables(
            DB,
            run_id,
            step_number
        )

        print("\n========== VARIABLES ==========\n")

        if variables:
            for name, value in variables:
                print(f"{name} = {value}")
        else:
            print("No variables recorded.")

    # -------------------------------
    # Replay Trace
    # -------------------------------
    elif choice == "2":

        run_id = int(input("Enter Run ID: "))

        replay_trace(DB, run_id)

    # -------------------------------
    # Search Variable
    # -------------------------------
    elif choice == "3":

        run_id = int(input("Enter Run ID: "))
        variable_name = input("Enter Variable Name: ")

        results = search_variable(
            DB,
            run_id,
            variable_name
        )

        if results:

            print("\n========== SEARCH RESULTS ==========\n")

            for step, line, value in results:
                print(
                    f"Step {step} | "
                    f"Line {line} | "
                    f"{variable_name} = {value}"
                )

        else:

            show_message(
                "Variable not found.",
                "red"
            )

    # -------------------------------
    # Export JSON
    # -------------------------------
    elif choice == "4":

        run_id = int(input("Enter Run ID: "))

        export_to_json(
            DB,
            run_id,
            "trace.json"
        )

        show_message(
            "Trace exported successfully!",
            "green"
        )

    # -------------------------------
    # Exit
    # -------------------------------
    elif choice == "5":

        show_message(
            "Thank you for using PyChronicle!",
            "cyan"
        )

        break

    # -------------------------------
    # Invalid Choice
    # -------------------------------
    else:

        show_message(
            "Invalid choice. Please try again.",
            "red"
        )
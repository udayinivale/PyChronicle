from pychronicle.ui import (
    show_title,
    show_menu,
    show_success,
    show_error,
    show_info,
    show_help,
    show_about,
    confirm_exit
)

from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

from pychronicle.replay import replay_trace
from pychronicle.exporter import export_to_json
from pychronicle.search import search_variable
from pychronicle.statistics import get_execution_statistics
from pychronicle.history import delete_run
from pychronicle.run_details import get_run_details
from pychronicle.compare import compare_runs
from pychronicle.compare_variables import compare_variables

DB = "pychronicle.db"

while True:

    show_title()
    show_menu()

    choice = input("\nEnter Choice: ")

    # ==================================
    # 1. View Runs
    # ==================================
    if choice == "1":

        runs = get_runs(DB)

        if not runs:
            show_error("No execution runs found.")
            continue

        print("\n========== AVAILABLE RUNS ==========\n")

        for run in runs:
            print(f"Run ID : {run[0]}")
            print(f"Script : {run[1]}")
            print(f"Started: {run[2]}")
            print("-" * 50)

        try:
            run_id = int(input("\nEnter Run ID: "))
        except ValueError:
            show_error("Invalid Run ID.")
            continue

        steps = get_execution_steps(DB, run_id)

        if not steps:
            show_error("No execution steps found.")
            continue

        print("\n========== EXECUTION STEPS ==========\n")

        for step in steps:
            print(
                f"Step {step[1]} | "
                f"Line {step[2]} | "
                f"Function: {step[3]} | "
                f"Event: {step[4]}"
            )

        try:
            step_number = int(input("\nEnter Step Number: "))
        except ValueError:
            show_error("Invalid Step Number.")
            continue

        step_id = None

        for step in steps:
            if step[1] == step_number:
                step_id = step[0]
                break

        if step_id is None:
            show_error("Step not found.")
            continue

        variables = get_variables(DB, step_id)

        print("\n========== VARIABLES ==========\n")

        if variables:
            for name, value in variables:
                print(f"{name} = {value}")
        else:
            print("No variables recorded.")

    # ==================================
    # 2. Replay Trace
    # ==================================
    elif choice == "2":

        run_id = int(input("Enter Run ID: "))
        replay_trace(DB, run_id)

    # ==================================
    # 3. Search Variable
    # ==================================
    elif choice == "3":

        run_id = int(input("Enter Run ID: "))
        variable = input("Variable Name: ")

        results = search_variable(DB, run_id, variable)

        if results:

            print("\n========== SEARCH RESULTS ==========\n")

            for step, line, value in results:
                print(
                    f"Step {step} | "
                    f"Line {line} | "
                    f"{variable} = {value}"
                )

        else:
            show_error("Variable not found.")

    # ==================================
    # 4. Statistics
    # ==================================
    elif choice == "4":

        run_id = int(input("Enter Run ID: "))

        stats = get_execution_statistics(DB, run_id)

        print("\n========== EXECUTION STATISTICS ==========\n")

        print(f"Total Steps      : {stats['total_steps']}")
        print(f"Total Variables  : {stats['total_variables']}")
        print(f"Unique Variables : {stats['unique_variables']}")

    # ==================================
    # 5. Export JSON
    # ==================================
    elif choice == "5":

        run_id = int(input("Enter Run ID: "))

        export_to_json(
            DB,
            run_id,
            "trace.json"
        )

        show_success("Trace exported successfully.")

    # ==================================
    # 6. Delete Run
    # ==================================
    elif choice == "6":

        run_id = int(input("Enter Run ID to delete: "))

        confirm = input(
            "Are you sure? (yes/no): "
        ).lower()

        if confirm == "yes":

            delete_run(DB, run_id)
            show_success("Execution run deleted successfully.")

        else:
            show_info("Deletion cancelled.")

    # ==================================
    # 7. Help
    # ==================================
    elif choice == "7":

        show_help()

    # ==================================
    # 8. About
    # ==================================
    elif choice == "8":

        show_about()


    # ==================================
    # 9. Run Details
    # ==================================
    elif choice == "9":

        run_id = int(input("Enter Run ID: "))
        details = get_run_details("pychronicle.db", run_id)

        if details:
            print(f"\n========== RUN DETAILS ==========")
            print(f"Run ID: {details['run_id']}")
            print(f"Script Path: {details['script_path']}")
            print(f"Started At: {details['started_at']}")
            print(f"Total Steps: {details['total_steps']}")
            print(f"Total Variables: {details['total_variables']}")
        else:
            show_error("Run not found.")

    # ==================================
    # 10. Compare Runs
    # ==================================
    elif choice == "10":

        run1 = int(input("Enter First Run ID: "))
        run2 = int(input("Enter Second Run ID: "))
        differences = compare_runs("pychronicle.db", run1, run2)

        if differences:
            print(f"\n========== COMPARISON RESULTS ==========")
            for diff in differences:
                print(f"Step {diff['step']}:")
                print(f"  Run 1: {diff['run1']}")
                print(f"  Run 2: {diff['run2']}")
        else:
            show_success("No differences found.")

    # ==================================
    # 11. Compare Variables
    # ==================================
    elif choice == "11":

        run1 = int(input("Enter First Run ID: "))
        run2 = int(input("Enter Second Run ID: "))
        differences = compare_variables("pychronicle.db", run1, run2)

        if differences:
            print(f"\n========== COMPARISON RESULTS ==========")
            for diff in differences:
                print(f"Step {diff['step']}:")
                print(f"  Variable: {diff['variable']}")
                print(f"  Run 1: {diff['run1']}")
                print(f"  Run 2: {diff['run2']}")
        else:
            show_success("No differences found.")

    # ==================================
    # 0. Exit
    # ==================================
    elif choice == "0":

        if confirm_exit():
            show_info("Thank you for using PyChronicle!")
            break

    # ==================================
    # Invalid Option
    # ==================================
    else:
        show_error("Invalid choice. Please try again.")
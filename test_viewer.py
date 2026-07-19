from pychronicle.viewer import (
    get_runs,
    get_execution_steps,
    get_variables
)

DB = "pychronicle.db"

print("Runs:")
print(get_runs(DB))

print("\nExecution Steps:")
print(get_execution_steps(DB, 7))

print("\nVariables at Step 3:")
print(get_variables(DB, 7, 3))
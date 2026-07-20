from pychronicle.viewer import (
    get_run_details,
    get_all_variables
)

DB = "pychronicle.db"

print("Run Details")
print(get_run_details(DB, 7))

print("\nAll Variables")

variables = get_all_variables(DB, 7)

for variable in variables:
    print(variable)
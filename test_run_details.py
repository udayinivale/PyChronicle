from pychronicle.run_details import get_run_details

details = get_run_details(
    "pychronicle.db",
    7
)

print(details)
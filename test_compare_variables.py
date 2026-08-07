from pychronicle.compare_variables import compare_variables

result = compare_variables(
    "pychronicle.db",
    7,
    2
)

for item in result:
    print(item)
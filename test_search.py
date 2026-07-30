from pychronicle.search import search_variable

result = search_variable(
    "pychronicle.db",
    7,
    "x"
)

for row in result:
    print(row)
from pychronicle.timeline import get_execution_timeline

timeline = get_execution_timeline(
    "pychronicle.db",
    7
)

for item in timeline:
    print(item)
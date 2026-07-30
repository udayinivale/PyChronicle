from pychronicle.statistics import get_execution_statistics

stats = get_execution_statistics(
    "pychronicle.db",
    7
)

print(stats)
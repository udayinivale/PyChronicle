from pychronicle.tracer import PyChronicleTracer

tracer = PyChronicleTracer(
    "example.py",
    "pychronicle.db"
)

tracer.trace_execution()

print("Tracing completed.")
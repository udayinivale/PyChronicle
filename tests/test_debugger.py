import os
import sqlite3
import sys
import unittest
from pychronicle.tracer import PyChronicleTracer
from pychronicle.ast_analyzer import analyze_script
from pychronicle import db

class TestPyChronicle(unittest.TestCase):
    def setUp(self):
        self.script_path = "temp_target.py"
        self.db_path = "test_trace.db"
        with open(self.script_path, "w", encoding="utf-8") as f:
            f.write("""
def calculate(a, b):
    result = a + b
    factor = 2
    for i in range(2):
        result = result * factor
    return result

x = 10
y = 20
z = calculate(x, y)
""")

    def tearDown(self):
        if os.path.exists(self.script_path):
            os.remove(self.script_path)
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_ast_analysis(self):
        analysis = analyze_script(self.script_path)
        variables = analysis["assigned_variables"]
        self.assertIn("x", variables)
        self.assertIn("y", variables)
        self.assertIn("z", variables)
        self.assertIn("calculate", variables)

    def test_tracer_and_db(self):
        tracer = PyChronicleTracer(self.script_path, self.db_path)
        tracer.trace_execution()
        self.assertTrue(os.path.exists(self.db_path))
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        steps = conn.execute("SELECT * FROM steps WHERE run_id = ? ORDER BY step_number ASC", (tracer.run_id,)).fetchall()
        self.assertGreater(len(steps), 0)
        conn.close()

if __name__ == "__main__":
    unittest.main()

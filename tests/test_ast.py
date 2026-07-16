import unittest
from unittest import result

from pychronicle.ast_analyzer import analyze_script


class TestAST(unittest.TestCase):

    def test_variable_detection(self):

        result = analyze_script("example.py")

        self.assertIn("x", result["assigned_variables"])
        self.assertIn("y", result["assigned_variables"])
        self.assertIn("total", result["assigned_variables"])

    def test_multiple_assignment(self):

        result = analyze_script("example.py")

        self.assertIn("a", result["assigned_variables"])
        self.assertIn("b", result["assigned_variables"])

    def test_list_assignment(self):

        result = analyze_script("example.py")

        self.assertIn("first", result["assigned_variables"])
        self.assertIn("second", result["assigned_variables"])
    def test_annotated_assignment(self):

        result = analyze_script("example.py")

        self.assertIn("age", result["assigned_variables"])

    def test_annotated_assignment(self):

        result = analyze_script("example.py")

        self.assertIn("age", result["assigned_variables"])

if __name__ == "__main__":
    unittest.main()
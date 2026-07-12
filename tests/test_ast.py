import unittest

from pychronicle.ast_analyzer import analyze_script


class TestAST(unittest.TestCase):

    def test_variable_detection(self):

        result = analyze_script("example.py")

        self.assertIn("x", result["assigned_variables"])
        self.assertIn("y", result["assigned_variables"])
        self.assertIn("total", result["assigned_variables"])


if __name__ == "__main__":
    unittest.main()
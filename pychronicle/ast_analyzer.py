import ast
from typing import Set, Dict, List, Any


class AssignmentFinder(ast.NodeVisitor):

    def __init__(self):
        self.assigned_vars: Set[str] = set()

    def _add_assignment(self, name: str):
        if name.isidentifier() and not name.startswith("__"):
            self.assigned_vars.add(name)

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self._add_assignment(target.id)

        self.generic_visit(node)


def analyze_script(file_path: str) -> Dict[str, Any]:

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    finder = AssignmentFinder()
    finder.visit(tree)

    return {
        "assigned_variables": sorted(list(finder.assigned_vars))
    }
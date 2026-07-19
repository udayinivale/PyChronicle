import ast
from platform import node
from typing import Set, Dict, List, Any


class AssignmentFinder(ast.NodeVisitor):

    def __init__(self):
        self.assigned_vars: Set[str] = set()
        self.line_assignments: Dict[int, List[str]] = {}

    def _add_assignment(self, name: str, lineno: int):

        if name.isidentifier() and not name.startswith("__"):

            self.assigned_vars.add(name)

            if lineno not in self.line_assignments:
                self.line_assignments[lineno] = []

            if name not in self.line_assignments[lineno]:
                self.line_assignments[lineno].append(name)
    
    def _parse_target(self, target: ast.AST, lineno: int):
        if isinstance(target, ast.Name):
            self._add_assignment(target.id, target.lineno)

        elif isinstance(target, (ast.Tuple, ast.List)):
            for element in target.elts:
                self._parse_target(element, lineno)

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            self._parse_target(target, node.lineno)

        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        """
        Handles annotated assignments.
        Example:
            age: int = 20
        """
        self._parse_target(node.target, node.lineno)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        """
        Handles augmented assignments.
        Example:
            total += 10
        """
        self._parse_target(node.target, node.lineno)
        self.generic_visit(node)

def analyze_script(file_path: str) -> Dict[str, Any]:

    try:

        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

    except FileNotFoundError:

        raise FileNotFoundError(
            f"{file_path} not found."
    )
        source = f.read()

    try:

        tree = ast.parse(source)

    except SyntaxError:

        raise

    finder = AssignmentFinder()
    finder.visit(tree)

    return {
        "assigned_variables": sorted(
            finder.assigned_vars
        ),
        "line_assignments": 
            finder.line_assignments
    }
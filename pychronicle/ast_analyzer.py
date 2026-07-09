import ast
from typing import Set, Dict, List, Any

class AssignmentFinder(ast.NodeVisitor):
    def __init__(self):
        self.assigned_vars: Set[str] = set()
        self.line_assignments: Dict[int, List[str]] = {}

    def _add_assignment(self, name: str, lineno: int):
        if not name.isidentifier() or name.startswith("__"):
            return
        self.assigned_vars.add(name)

def analyze_script(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, filename=file_path)
    finder = AssignmentFinder()
    finder.visit(tree)
    return {
        "assigned_variables": sorted(list(finder.assigned_vars)),
        "line_assignments": finder.line_assignments,
        "source_code": source
    }

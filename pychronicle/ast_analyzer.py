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
        if lineno not in self.line_assignments:
            self.line_assignments[lineno] = []
        if name not in self.line_assignments[lineno]:
            self.line_assignments[lineno].append(name)

    def _parse_target(self, target: ast.AST, lineno: int):
        if isinstance(target, ast.Name):
            self._add_assignment(target.id, lineno)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self._parse_target(elt, lineno)
        elif isinstance(target, ast.Attribute):
            self._parse_target(target.value, lineno)

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            self._parse_target(target, node.lineno)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign):
        self._parse_target(node.target, node.lineno)
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign):
        self._parse_target(node.target, node.lineno)
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        self._parse_target(node.target, node.lineno)
        self.generic_visit(node)

    def visit_arg(self, node: ast.arg):
        self._add_assignment(node.arg, node.lineno)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._add_assignment(node.name, node.lineno)
        self.generic_visit(node)

def analyze_script(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    try:
        tree = ast.parse(source, filename=file_path)
    except SyntaxError as e:
        raise ValueError(f"Syntax error in target script: {e.msg} at line {e.lineno}")
        
    finder = AssignmentFinder()
    finder.visit(tree)
    return {
        "assigned_variables": sorted(list(finder.assigned_vars)),
        "line_assignments": finder.line_assignments,
        "source_code": source
    }

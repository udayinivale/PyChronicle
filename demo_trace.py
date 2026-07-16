from pychronicle.ast_analyzer import analyze_script

result = analyze_script("example.py")

print("\nVariables")
print(result["assigned_variables"])

print("\nAssignments by line")

for line, variables in result["line_assignments"].items():
    print(f"Line {line}: {variables}")
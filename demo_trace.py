import sqlite3
from pychronicle.tracer import PyChronicleTracer
from pychronicle.ast_analyzer import analyze_script

def run_demo():
    script_path = "example.py"
    db_path = "example_trace.db"
    
    print("[*] Running AST Analysis on example.py...")
    analysis = analyze_script(script_path)
    print(f"Statically identified variables: {analysis['assigned_variables']}")
    print("-" * 70)
    
    print("[*] Executing example.py under tracer control...")
    tracer = PyChronicleTracer(script_path, db_path)
    tracer.trace_execution()
    print(f"[+] Execution trace saved. Total steps recorded: {tracer.step_number}")
    print("-" * 70)
    
    # Query database and print logs
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    print(f"{'Step':<5} | {'Line':<5} | {'Event':<8} | {'Function':<18} | {'Variable Changes (Deltas)'}")
    print("=" * 85)
    
    steps = conn.execute("SELECT * FROM steps ORDER BY step_number ASC").fetchall()
    for step in steps:
        step_id = step["step_id"]
        step_num = step["step_number"]
        line_num = step["line_number"]
        event = step["event"]
        func = step["function_name"]
        
        # Get variables mutated at this step
        deltas = conn.execute(
            "SELECT variable_name, serialized_value FROM variable_states WHERE step_id = ?",
            (step_id,)
        ).fetchall()
        
        delta_str = ", ".join([f"{d['variable_name']}={d['serialized_value']}" for d in deltas])
        if not delta_str:
            delta_str = "(no change)"
            
        print(f"{step_num:<5} | {line_num:<5} | {event:<8} | {func:<18} | {delta_str}")
        
    conn.close()

if __name__ == "__main__":
    run_demo()

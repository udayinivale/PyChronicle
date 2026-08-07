import sqlite3


def generate_report(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT script_path, started_at
        FROM runs
        WHERE run_id = ?
    """, (run_id,))

    run = cursor.fetchone()

    if run is None:
        conn.close()
        return None

    script_path, started_at = run

    cursor.execute("""
        SELECT COUNT(*)
        FROM execution_steps
        WHERE run_id = ?
    """, (run_id,))
    total_steps = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(DISTINCT variable_name)
        FROM variables
        WHERE run_id = ?
    """, (run_id,))
    unique_variables = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM variables
        WHERE run_id = ?
    """, (run_id,))
    total_variables = cursor.fetchone()[0]

    conn.close()

    return {
        "run_id": run_id,
        "script": script_path,
        "started_at": started_at,
        "steps": total_steps,
        "variables": total_variables,
        "unique_variables": unique_variables
    }
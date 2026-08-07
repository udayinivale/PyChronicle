import sqlite3


def get_run_details(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            run_id,
            script_path,
            started_at
        FROM runs
        WHERE run_id = ?
    """, (run_id,))

    run = cursor.fetchone()

    if run is None:
        conn.close()
        return None

    cursor.execute("""
        SELECT COUNT(*)
        FROM execution_steps
        WHERE run_id = ?
    """, (run_id,))

    total_steps = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM variables
        WHERE run_id = ?
    """, (run_id,))

    total_variables = cursor.fetchone()[0]

    conn.close()

    return {
        "run_id": run[0],
        "script_path": run[1],
        "started_at": run[2],
        "total_steps": total_steps,
        "total_variables": total_variables
    }
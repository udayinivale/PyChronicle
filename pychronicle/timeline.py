import sqlite3


def get_execution_timeline(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            step_number,
            line_number
        FROM execution_steps
        WHERE run_id = ?
        ORDER BY step_number
    """, (run_id,))

    rows = cursor.fetchall()
    conn.close()

    timeline = []

    for step, line in rows:
        timeline.append({
            "step": step,
            "line": line
        })

    return timeline
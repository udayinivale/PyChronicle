import sqlite3


def compare_runs(db_path, run1, run2):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT step_number, line_number
        FROM execution_steps
        WHERE run_id = ?
        ORDER BY step_number
    """, (run1,))
    steps1 = cursor.fetchall()

    cursor.execute("""
        SELECT step_number, line_number
        FROM execution_steps
        WHERE run_id = ?
        ORDER BY step_number
    """, (run2,))
    steps2 = cursor.fetchall()

    conn.close()

    differences = []

    max_steps = max(len(steps1), len(steps2))

    for i in range(max_steps):

        s1 = steps1[i] if i < len(steps1) else None
        s2 = steps2[i] if i < len(steps2) else None

        if s1 != s2:
            differences.append(
                {
                    "step": i + 1,
                    "run1": s1,
                    "run2": s2
                }
            )

    return differences
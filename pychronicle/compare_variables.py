import sqlite3


def compare_variables(db_path, run1, run2):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT step_number,
               variable_name,
               variable_value
        FROM variables
        WHERE run_id = ?
        ORDER BY step_number
    """, (run1,))
    vars1 = cursor.fetchall()

    cursor.execute("""
        SELECT step_number,
               variable_name,
               variable_value
        FROM variables
        WHERE run_id = ?
        ORDER BY step_number
    """, (run2,))
    vars2 = cursor.fetchall()

    conn.close()

    dict1 = {(s, n): v for s, n, v in vars1}
    dict2 = {(s, n): v for s, n, v in vars2}

    keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    differences = []

    for key in keys:

        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if value1 != value2:

            differences.append({
                "step": key[0],
                "variable": key[1],
                "run1": value1,
                "run2": value2
            })

    return differences
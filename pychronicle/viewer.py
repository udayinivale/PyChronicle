import sqlite3

def get_runs(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT run_id, script_path, started_at
        FROM runs
        ORDER BY run_id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
def get_execution_steps(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT step_number, line_number
        FROM execution_steps
        WHERE run_id = ?
        ORDER BY step_number
    """, (run_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows
def get_variables(db_path, run_id, step_number):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT variable_name, variable_value
        FROM variables
        WHERE run_id = ? AND step_number = ?
    """, (run_id, step_number))

    rows = cursor.fetchall()

    conn.close()

    return rows
import sqlite3


def get_run_details(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT run_id, script_path, started_at
        FROM runs
        WHERE run_id = ?
    """, (run_id,))

    row = cursor.fetchone()

    conn.close()

    return row
def get_all_variables(db_path, run_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT step_number,
               variable_name,
               variable_value
        FROM variables
        WHERE run_id = ?
        ORDER BY step_number
    """, (run_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows
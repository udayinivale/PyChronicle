import sqlite3
import time


def get_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path):
    conn = get_connection(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs(
        run_id INTEGER PRIMARY KEY AUTOINCREMENT,
        script_path TEXT,
        started_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_run(db_path, script_path):
    conn = get_connection(db_path)

    cursor = conn.cursor()

    started_at = time.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO runs(script_path, started_at)
        VALUES(?, ?)
        """,
        (script_path, started_at)
    )

    conn.commit()

    run_id = cursor.lastrowid

    conn.close()

    return run_id
def insert_step(db_path, run_id, step_number, line_number):

    conn = get_connection(db_path)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS execution_steps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER,
            step_number INTEGER,
            line_number INTEGER
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO execution_steps(run_id, step_number, line_number)
        VALUES(?,?,?)
        """,
        (run_id, step_number, line_number)
    )

    conn.commit()

    conn.close()


def insert_variables(db_path, run_id, step_number, variables):

    conn = get_connection(db_path)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS variables(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER,
            step_number INTEGER,
            variable_name TEXT,
            variable_value TEXT
        )
        """
    )

    for name, value in variables.items():

        cursor.execute(
            """
            INSERT INTO variables(
                run_id,
                step_number,
                variable_name,
                variable_value
            )
            VALUES(?,?,?,?)
            """,
            (
                run_id,
                step_number,
                name,
                str(value)
            )
        )

    conn.commit()

    conn.close()
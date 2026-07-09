import sqlite3
import time
from typing import List, Dict, Any, Tuple, Optional

def get_connection(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str):
    conn = get_connection(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        
        # Table to store execution runs
        conn.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                run_id INTEGER PRIMARY KEY AUTOINCREMENT,
                script_path TEXT NOT NULL,
                started_at TEXT NOT NULL
            );
        """)
        
        # Table to store line-by-line execution steps
        conn.execute("""
            CREATE TABLE IF NOT EXISTS steps (
                step_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id INTEGER NOT NULL,
                step_number INTEGER NOT NULL,
                line_number INTEGER NOT NULL,
                function_name TEXT NOT NULL,
                event TEXT NOT NULL,
                timestamp REAL NOT NULL,
                FOREIGN KEY(run_id) REFERENCES runs(run_id) ON DELETE CASCADE
            );
        """)
        # Table to store variable state mutations (deltas)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS variable_states (
                state_id INTEGER PRIMARY KEY AUTOINCREMENT,
                step_id INTEGER NOT NULL,
                variable_name TEXT NOT NULL,
                variable_type TEXT NOT NULL,
                serialized_value TEXT NOT NULL,
                is_delta INTEGER DEFAULT 1,
                FOREIGN KEY(step_id) REFERENCES steps(step_id) ON DELETE CASCADE
            );
        """)
        # Create indexes for performance
        conn.execute("CREATE INDEX IF NOT EXISTS idx_steps_run ON steps(run_id, step_number);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_step ON variable_states(step_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_lookup ON variable_states(variable_name, step_id);")
        conn.commit()
    finally:
        conn.close()

def create_run(db_path: str, script_path: str) -> int:
    started_at = time.strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO runs (script_path, started_at) VALUES (?, ?)", (script_path, started_at))
        # Create indexes for performance
        conn.execute("CREATE INDEX IF NOT EXISTS idx_steps_run ON steps(run_id, step_number);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_step ON variable_states(step_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_lookup ON variable_states(variable_name, step_id);")
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()

def insert_step(db_path: str, run_id: int, step_number: int, line_number: int, 
                function_name: str, event: str, timestamp: float) -> int:
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO steps (run_id, step_number, line_number, function_name, event, timestamp)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (run_id, step_number, line_number, function_name, event, timestamp)
        )
        # Create indexes for performance
        conn.execute("CREATE INDEX IF NOT EXISTS idx_steps_run ON steps(run_id, step_number);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_step ON variable_states(step_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_lookup ON variable_states(variable_name, step_id);")
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()

def insert_variable_states(db_path: str, step_id: int, variables: List[Tuple[str, str, str]]):
    if not variables:
        return
    conn = get_connection(db_path)
    try:
        conn.executemany(
            "INSERT INTO variable_states (step_id, variable_name, variable_type, serialized_value, is_delta) VALUES (?, ?, ?, ?, 1)",
            [(step_id, name, v_type, val) for name, v_type, val in variables]
        )
        # Create indexes for performance
        conn.execute("CREATE INDEX IF NOT EXISTS idx_steps_run ON steps(run_id, step_number);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_step ON variable_states(step_id);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_lookup ON variable_states(variable_name, step_id);")
        conn.commit()
    finally:
        conn.close()

def get_run_steps(db_path: str, run_id: int) -> List[Dict[str, Any]]:
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM steps WHERE run_id = ? ORDER BY step_number ASC", (run_id,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()

def get_variable_states_at_step(db_path: str, step_id: int) -> Dict[str, Dict[str, str]]:
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT vs.variable_name, vs.variable_type, vs.serialized_value
            FROM variable_states vs
            INNER JOIN (
                SELECT variable_name, MAX(step_id) as max_step_id
                FROM variable_states
                WHERE step_id <= ?
                GROUP BY variable_name
            ) latest ON vs.variable_name = latest.variable_name AND vs.step_id = latest.max_step_id
            """,
            (step_id,)
        )
        return {
            row["variable_name"]: {"type": row["variable_type"], "value": row["serialized_value"]}
            for row in cursor.fetchall()
        }
    finally:
        conn.close()

def delete_run(db_path: str, run_id: int):
    conn = get_connection(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("DELETE FROM runs WHERE run_id = ?", (run_id,))
        conn.commit()
    finally:
        conn.close()

def optimize_db(db_path: str):
    conn = get_connection(db_path)
    try:
        conn.execute("PRAGMA optimize;")
        conn.commit()
    finally:
        conn.close()

def get_variable_history(db_path: str, run_id: int, variable_name: str) -> List[Dict[str, Any]]:
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT s.step_number, s.line_number, vs.serialized_value, vs.variable_type, s.timestamp
            FROM variable_states vs
            INNER JOIN steps s ON vs.step_id = s.step_id
            WHERE s.run_id = ? AND vs.variable_name = ?
            ORDER BY s.step_number ASC
            """,
            (run_id, variable_name)
        )
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()

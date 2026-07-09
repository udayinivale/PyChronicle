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
        conn.commit()
    finally:
        conn.close()

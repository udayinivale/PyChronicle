import sqlite3
import time
from typing import List, Dict, Any, Tuple, Optional

def get_connection(db_path: str) -> sqlite3.Connection:
    """Helper function to open a connection to the SQLite database."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# ==========================================
# WEEK 1 - DAY 1: Create Database Schema
# ==========================================
def init_db(db_path: str):
    """Initializes the database connection, enables foreign key constraints,
    and calls table creation routines."""
    conn = get_connection(db_path)
    try:
        # Enable Foreign Key support in SQLite
        conn.execute("PRAGMA foreign_keys = ON;")
        
        # Call table creation functions (Day 2)
        _create_tables(conn)
        _create_indexes(conn)
        
        conn.commit()
    finally:
        conn.close()

# ==========================================
# WEEK 1 - DAY 2: Add Tables & Indexes
# ==========================================
def _create_tables(conn: sqlite3.Connection):
    """Creates all required tables for tracking runs, steps, and variables."""
    
    # 1. Table to store execution runs
    conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            script_path TEXT NOT NULL,
            started_at TEXT NOT NULL
        );
    """)
    
    # 2. Table to store line-by-line execution steps
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

    # 3. Table to store variable state mutations (deltas)
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

def _create_indexes(conn: sqlite3.Connection):
    """Creates performance indexes for fast step and variable querying."""
    conn.execute("CREATE INDEX IF NOT EXISTS idx_steps_run ON steps(run_id, step_number);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_step ON variable_states(step_id);")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_var_states_lookup ON variable_states(variable_name, step_id);")
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
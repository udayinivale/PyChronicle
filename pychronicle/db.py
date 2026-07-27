def get_all_runs():
    """
    Return all execution runs.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, script_name, start_time, end_time
        FROM runs
        ORDER BY id DESC
    """)

    runs = cursor.fetchall()
    conn.close()
    return runs


def get_run_by_id(run_id):
    """
    Return one run by its ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM runs
        WHERE id = ?
    """, (run_id,))

    run = cursor.fetchone()
    conn.close()
    return run


def search_runs(keyword):
    """
    Search runs using script name.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, script_name, start_time, end_time
        FROM runs
        WHERE script_name LIKE ?
        ORDER BY id DESC
    """, (f"%{keyword}%",))

    results = cursor.fetchall()
    conn.close()
    return results


def delete_all_runs():
    """
    Delete every run from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM variable_states")
    cursor.execute("DELETE FROM steps")
    cursor.execute("DELETE FROM runs")

    conn.commit()
    conn.close()

    return True


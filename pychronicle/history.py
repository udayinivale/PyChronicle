import sqlite3


def delete_run(db_path, run_id):
    conn = sqlite3.connect(db_path)

    # Enable foreign keys
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM runs WHERE run_id = ?",
        (run_id,)
    )

    conn.commit()
    conn.close()

    return True
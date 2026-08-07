import os


def validate_project(db_path):
    report = {
        "database_exists": False,
        "total_runs": 0,
        "status": "FAILED"
    }

    if not os.path.exists(db_path):
        return report

    import sqlite3

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    report["database_exists"] = True

    cursor.execute("SELECT COUNT(*) FROM runs")
    report["total_runs"] = cursor.fetchone()[0]

    conn.close()

    report["status"] = "SUCCESS"

    return report
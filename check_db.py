import sqlite3

conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

cursor.execute("SELECT MAX(run_id) FROM runs")
latest_run = cursor.fetchone()[0]

print("Latest Run:", latest_run)

print("\nVariables:")
cursor.execute("""
SELECT step_number, variable_name, variable_value
FROM variables
WHERE run_id = ?
ORDER BY step_number, variable_name
""", (latest_run,))

for row in cursor.fetchall():
    print(row)

conn.close()
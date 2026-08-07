import sqlite3

conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

print("Runs")
cursor.execute("SELECT * FROM runs")
print(cursor.fetchall())

print("\nExecution Steps")
cursor.execute("SELECT * FROM execution_steps")
print(cursor.fetchall())

print("\nVariables")
cursor.execute("SELECT * FROM variables")
print(cursor.fetchall())

conn.close()
# Making Table
import sqlite3

db_location = "data12.db"
connection = sqlite3.connect(db_location)
cursor = connection.cursor()

create_table = "CREATE TABLE data12 (ID INTEGER,Task TEXT NOT NULL,Status TEXT, PRIMARY KEY(ID));"
cursor.execute(create_table)
cursor.execute(f"INSERT INTO data12(ID,Task,Status) VALUES('1', 'Water Plant', 'Not Started')")
cursor.execute(f"INSERT INTO data12(ID,Task,Status) VALUES('2', 'Go to Bank', 'Not Started')")

connection.commit()
connection.close()
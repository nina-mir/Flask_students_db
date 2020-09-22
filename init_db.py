import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

examples = [(2, "Nina","Obama"), (32, "Nina", "Hitachi"), (425, "Nina", "Lenovo")]

cur.executemany("INSERT INTO students (id, fname, lname) VALUES (?, ?, ?)", examples)

connection.commit()
connection.close()

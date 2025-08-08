import sqlite3
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name Text, surname Text, bdate Text, number TEXT UNIQUE, major Text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS lessons (name Text, credit Integer, major Text)")
    conn.commit()
    conn.close()

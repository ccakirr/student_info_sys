import sqlite3
def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name Text, surname Text, bdate Text, number TEXT UNIQUE, major Text)")
    cursor.execute("CREATE TABLE IF NOT EXISTS lessons (name Text, credit Integer, major Text)")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students_lessons (
    stu_number  TEXT NOT NULL,
    stu_lessons TEXT NOT NULL,
    stu_major Text Not Null,
    PRIMARY KEY (stu_number, stu_lessons,stu_major),
    FOREIGN KEY (stu_number)  REFERENCES students(number),
    FOREIGN KEY (stu_lessons) REFERENCES lessons(name)
    );""")
    conn.commit()
    conn.close()

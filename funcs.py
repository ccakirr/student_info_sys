import sqlite3
import random
import datetime

class StudentManagement():
    def __init__(self, con):
        self.conn = con
        self.cursor = con.cursor()
    def addstudent(self, name, surname, bdate, number, major):
        self.cursor.execute(f"insert into students values (?, ?, ?, ?, ?)", (name, surname, bdate, number, major))
        self.conn.commit()

    def editstudent(self, number, name, newname):
        pass

    def delstudent(self, number):
        pass

    def liststudent(self):
        pass

    def generate_student_number(self):
        year = datetime.datetime.now().year
        while True:
            number = f"{year}{random.randint(100000, 999999)}"
            self.cursor.execute("SELECT 1 FROM students WHERE number = ?", (number,))
            if not self.cursor.fetchone():
                return number


class LessonManagement():
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    def addlesson(self, name, credit, major):
        self.cursor.execute("Select * from lessons Where name = ? and credit = ? and major = ?", (name, credit, major))
        if(self.cursor.fetchone()):
           print("Bu ders kaydı zaten bulunmakta.")
        else:
           self.cursor.execute(f"insert into lessons values(?, ?, ?)",(name, credit, major))
           self.conn.commit()

    def dellesson(self, name):


         pass


    def listlesson(self):
        pass



class RecManagement():
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    def givelesson(self, major, number, lesson):
        pass

    def listgivenlessons(self, number,):
        pass


    def delgivenlesson(self, number, lesson):
        pass

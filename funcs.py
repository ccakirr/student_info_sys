import random
import datetime

class StudentManagement():
    def __init__(self, con):
        self.conn = con
        self.cursor = con.cursor()
    def addstudent(self, name, surname, bdate, number, major):
        self.cursor.execute("insert into students values (?, ?, ?, ?, ?)", (name, surname, bdate, number, major,))
        self.conn.commit()

    def editstudent(self, number, newname):
        self.cursor.execute("Update students set name = ? where number = ?", (newname, number,))
        self.conn.commit()

    def delstudent(self, number):
        self.cursor.execute("Delete from students where number = ?", (number,))
        self.conn.commit()

    def liststudent(self):
        self.cursor.execute("Select * from students")
        students = self.cursor.fetchall()
        print("-----Öğrenciler-----")
        for student in students:
            print(f"Ad: {student[0]} {student[1]} | Bölüm: {student[4]} | Numara: {student[3]} | Doğum Tarihi: {student[2]}")

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
        self.cursor.execute("Select * from lessons Where name = ? and credit = ? and major = ?", (name, credit, major,))
        if(self.cursor.fetchone()):
           print("Bu ders kaydı zaten bulunmakta.")
        else:
           self.cursor.execute("insert into lessons values(?, ?, ?)",(name, credit, major))
           self.conn.commit()

    def dellesson(self, name):
        self.cursor.execute("Delete from lessons where name = ?", (name))
        self.conn.commit()


    def listlesson(self):
        self.cursor.execute("Select * from lessons")
        print("-----Dersler-----")
        for lesson in self.cursor.fetchall():
            print(f"Ders adı: {lesson[0]} | Ders kredisi: {lesson[1]} | Dersin bölümü {lesson[2]}")




class RecManagement():
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    def givelesson(self, number, lesson, major):
        self.cursor.execute("Insert into students_lessons values(?, ?, ?,)", (number, lesson, major,))
        self.conn.commit()
    def give_lesson_to_major(self, major, lesson):
        self.cursor.execute("Select major = ? from students",(major))
        major_students = self.cursor.fetchall()
        for student in major_students:
            self.cursor.execute("Insert into students_lessons values(?, ?, ?)", student[3], lesson, major,)
    def listgivenlessons(self, number):
        self.cursor.execute("Select * from students_lessons where number = ?", (number,))
        student_lesson = self.cursor.fetchall()
        self.cursor.execute("Select name, surname from students where number = ?", (number,))
        student = self.cursor.fetchone()
        if not student:
            print("Öğrenci yok.")
            return
        print("Adı: " + student[0] + "Soyadı: " + student[1] + "Aldığı dersler:")
        for lesson in student_lesson:
            print(lesson[1])


    def delgivenlesson(self, number, lesson):
        self.cursor.execute("Delete from students_lessons Where number = ? and lesson = ?", (number, lesson,))
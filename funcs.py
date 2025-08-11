import random
import datetime

class StudentManagement():
    def __init__(self, con):
        self.conn = con
        self.cursor = con.cursor()

    def addstudent(self):
        name = input("Ad: ")
        surname = input("Soyad: ")
        bdate = input("Doğum tarihi (YYYY-AA-GG): ")
        major = input("Bölüm: ")
        number = self.generate_student_number()
        self.cursor.execute(
            "insert into students values (?, ?, ?, ?, ?)",
            (name, surname, bdate, number, major)
        )
        self.conn.commit()
        print(f"Öğrenci eklendi. Otomatik numara: {number}")

    def editstudent(self):
        number = input("Öğrenci numarası: ")
        newname = input("Yeni isim: ")
        self.cursor.execute("Update students set name = ? where number = ?", (newname, number,))
        self.conn.commit()

    def delstudent(self):
        number = input("Silinecek öğrenci numarası: ")
        self.cursor.execute("Delete from students where number = ?", (number,))
        self.conn.commit()

    def liststudent(self):
        self.cursor.execute("Select * from students")
        students = self.cursor.fetchall()
        print("-----Öğrenciler-----")
        for student in students:
            print(f"Ad: {student[0]} {student[1]} | Bölüm: {student[4]} | Numara: {student[3]} | Doğum Tarihi: {student[2]}")

    def generate_student_number(self):
        import random
        import datetime
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

    def addlesson(self):
        name = input("Ders adı: ")
        credit = input("Kredi: ")
        major = input("Bölüm: ")
        self.cursor.execute("Select * from lessons Where name = ? and credit = ? and major = ?", (name, credit, major,))
        if(self.cursor.fetchone()):
            print("Bu ders kaydı zaten bulunmakta.")
        else:
            self.cursor.execute("insert into lessons values(?, ?, ?)", (name, credit, major))
            self.conn.commit()

    def dellesson(self):
        name = input("Silinecek ders adı: ")
        self.cursor.execute("Delete from lessons where name = ?", (name,))
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

    def givelesson(self):
        number = input("Öğrenci numarası: ")
        lesson = input("Ders adı: ")
        major = input("Bölüm: ")
        self.cursor.execute(
            "INSERT INTO students_lessons (stu_number, stu_lessons, stu_major) VALUES (?, ?, ?)",
            (number, lesson, major)
        )
        self.conn.commit()

    def give_lesson_to_major(self):
        major = input("Bölüm: ")
        lesson = input("Ders adı: ")
        self.cursor.execute("SELECT * FROM students WHERE major = ?", (major,))
        major_students = self.cursor.fetchall()
        for student in major_students:
            self.cursor.execute(
                "INSERT INTO students_lessons (stu_number, stu_lessons, stu_major) VALUES (?, ?, ?)",
                (student[3], lesson, major)  # student[3] = number
            )
        self.conn.commit()

    def listgivenlessons(self):
        number = input("Öğrenci numarası: ")
        self.cursor.execute("SELECT * FROM students_lessons WHERE stu_number = ?", (number,))
        student_lesson = self.cursor.fetchall()
        self.cursor.execute("SELECT name, surname FROM students WHERE number = ?", (number,))
        student = self.cursor.fetchone()
        if not student:
            print("Öğrenci yok.")
            return
        print(f"Adı: {student[0]} Soyadı: {student[1]} Aldığı dersler:")
        for lesson in student_lesson:
            print(lesson[1])  # lesson[1] = stu_lessons

    def delgivenlesson(self):
        number = input("Öğrenci numarası: ")
        lesson = input("Silinecek ders adı: ")
        self.cursor.execute(
            "DELETE FROM students_lessons WHERE stu_number = ? AND stu_lessons = ?",
            (number, lesson)
        )
        self.conn.commit()


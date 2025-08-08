import sqlite3
import random
import sys
import datetime

class StudentManagement():
    def addstudent(self, name, surname, bdate, number, major):

    def editstudent(self, number, name, newname):

    def delstudent(self, number):

    def liststudent(self):

    def generate_student_number(self):
        year = datetime.datetime.now().year
        number = f"{year}{random.randint(100000, 999999)}"


class LessonManagement():
    def addlesson(self, name, credit, major):

    def dellesson(self, name):

    def listlesson(self):

class RecManagement():
    def givelesson(self, major, number, lesson):

    def listgivenlessons(self, number,):

    def delgivenlesson(self, number, lesson):

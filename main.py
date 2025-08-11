import funcs
import setup
import sqlite3

conn = sqlite3.connect("database.db")
setup.init_db()
stuman = funcs.StudentManagement(conn)
recman = funcs.RecManagement(conn)
lesman = funcs.LessonManagement(conn)
operations = {
	1:"Öğrenci ekle",
	2:"Öğrenci sil",
	3:"Öğrenci adını düzenle",
	4:"Öğrencileri listele",
	5:"Ders ekle",
	6:"Ders sil",
	7:"Dersleri listele",
	8:"Öğrenciye ders ata",
	9:"Bölüme ders ata",
	10:"Öğrenciye atanan dersi sil",
	11:"Öğrencinin aldığı dersleri listele",
	12: "Çıkış"
}
menu = {
	1:stuman.addstudent,
	2:stuman.delstudent,
	3:stuman.editstudent,
	4:stuman.liststudent,
	5:lesman.addlesson,
	6:lesman.dellesson,
	7:lesman.listlesson,
	8:recman.givelesson,
	9:recman.give_lesson_to_major,
	10:recman.delgivenlesson,
	11:recman.listgivenlessons,
	12:lambda: exit(0)
}
while (True):
	print("Lütfen yapmak istediğiniz işlemi seçin")
	for i in operations:
		print(f"{i}. {operations[i]}")
	try:
		secim = int(input("Seçiminizi giriniz (1-11): "))
	except ValueError:
		print("Lütfen geçerli bir sayı giriniz.")
		continue
	if secim not in menu:
		print("Lütfen geçerli bir işlem seçiniz.")
		continue
	else:
		menu[secim]()
	







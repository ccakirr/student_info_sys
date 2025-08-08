import funcs
import sqlite3

stuman = funcs.StudentManagement()
recman = funcs.RecManagement()
lesman = funcs.LessonManagement()
operations = {
	1:"Öğrenci ekle",
	2:"Öğrenci sil",
	3:"Öğrenci adını düzenle",
	4:"Öğrencileri listele",
	5:"Ders ekle",
	6:"Ders sil",
	7:"Dersleri listele",
	8:"Öğrenciye / Bölüme ders ata",
	9:"Öğrenciye / Bölüme atanan dersi sil",
	10:"Öğrencinin aldığı dersleri listele",
	11: "Çıkış"
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
	if secim not in operations:
		print("Lütfen geçerli bir işlem seçiniz.")
		continue
	if secim == 1:
		name = input("Öğrenci adı: ")
		surname = input("Öğrenci soyadı: ")
		bdate = input("Öğrenci doğum tarihi (GG.AA.YYYY şeklinde noktalarla birlikte): ")
		number = stuman.generate_student_number()
		major = input("Öğrenci bölümü: ")
		stuman.addstudent(name, surname, bdate, number, major)
	if secim == 2:
		number = input("Lütfen silmek istediğiniz öğrencinin numarasını girin: ")
		stuman.delstudent(number)
	







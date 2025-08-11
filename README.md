# Student Information System

A simple Python-based student information management system with SQLite integration.  
Supports student, lesson, and assignment (record) management.

## Features
- Add, edit, delete students
- Add, delete lessons
- Assign lessons to students or entire majors
- List all students, lessons, and assigned lessons
- Auto-generate unique student numbers
- Data stored in SQLite database with foreign key relationships

## Installation

```bash
git clone https://github.com/ccakirr/student-info-system.git
cd student-info-system
python main.py
```

## Requirements
- Python 3.x
- SQLite (bundled with Python)
- No additional libraries required

## Database Structure
**students**
- name
- surname
- bdate
- number (Primary Key)
- major

**lessons**
- name
- credit
- major

**students_lessons**
- stu_number (FK → students.number)
- stu_lessons (FK → lessons.name)
- stu_major

## Usage
Run the `main.py` file and follow the menu options to manage students and lessons.

## License
This project is licensed under the MIT License.

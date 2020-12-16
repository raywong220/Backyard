from sys import argv
from cs50 import SQL


if len(argv) != 2:
    print('Error')
    exit()
else:
    house = argv[1]

db = SQL("sqlite:///students.db")
students = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)
for student in students:
    if student['middle'] != None:
        print(student['first'], student['middle'], student['last'] + ', born', student['birth'])
    else:
        print(student['first'], student['last'] + ', born', student['birth'])

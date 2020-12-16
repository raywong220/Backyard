import csv
from sys import argv
from cs50 import SQL

if len(argv) != 2:
    print('Error')
    exit()
else:
    studentcsv = argv[1]

db = SQL("sqlite:///students.db")

with open(studentcsv,'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        fullname = row['name'].split()
        middle = None
        if len(fullname) == 3:
            middle = fullname[1]
        first, last = fullname[0], fullname[-1]
        house = row['house']
        birth = row['birth']
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)
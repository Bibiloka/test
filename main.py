import csv
from idlelib.iomenu import encoding

try:
    with open("Attendance.csv",'r', encoding ="utf-8") as file:
        reader = csv.reader(file,delimiter=',')
        titles = next(reader)
        students = []
        for student in reader:
            a = [student[0],int(student[1]),int(student[2]),int(student[3]),int(student[4])]
            students.append(a)
except FileNotFoundError:
    exit("file not found lol")

f = open("Ansver.txt",'w',encoding = "utf-8")

maxin = 0
for stud in students:
    if stud[1]+stud[2]+stud[3]+stud[4] > maxin:
        maxin = stud[1]+stud[2]+stud[3]+stud[4]

for stud in students:
    if stud[1]+stud[2]+stud[3]+stud[4] == maxin:
        f.write(stud[0] + " ")
f.write("\n")

PE = 0
count = 0
for stud in students:
    PE += stud[4]
    count+=1
PE = int(PE/count)
f.write(str(PE) + "\n")

algebra = 0
code = 0
math = 0
for stud in students:
    code += stud[1]
    math += stud[2]
    algebra += stud[4]

if PE > algebra and PE > code and PE > math:
    f.write("PE")
elif algebra > PE and algebra > code and algebra > math:
    f.write("algebra")
elif code > PE and code > math and code > algebra:
    f.write("code")
else:
    f.write("math")

f.close()
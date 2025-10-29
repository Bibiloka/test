import json

# try:
#     with open("animals.json", "r") as file:
#         animals = json.load(file)["animals"]
# except FileNotFoundError:
#     exit("File not found lol")
# except json.decoder.JSONDecodeError:
#     exit("json file cant be read")
#
# an_list = list(filter(lambda x: x['animal_type'] == 'Bird',animals))
# for bird in an_list:
#     print(bird)
#
# time_list = list(filter(lambda x: x['active_time'] == "Diurnal",animals))
# print(len(time_list))
#
# min_animal = min(animals, key = lambda x: x['weight_min'])["name"]
# print(min_animal)

try:
    with open("Grades.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    exit("File not found lol")
except json.decoder.JSONDecodeError:
    exit("json cant be read")

students2 = []
for i in range(len(students)):
    stud = {}
    stud["name"] = students[i]["student_name"]
    stud["averange"] = (students[i]["test1_score"]+students[i]["test2_score"]+students[i]["test3_score"])/3
    students2.append(stud)

with open("f.json",'w') as file:
    json.dump(students2, file)

ball = int(input("input yor ball:"))

students3 = []
for i in range(len(students2)):
    if students2[i]["averange"]*3 < ball:
        students3.append(students2[i])

with open("f.json",'w') as file:
    json.dump(students3, file)




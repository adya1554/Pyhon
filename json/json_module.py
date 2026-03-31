import json
students = {
    'student': {"rollno": 10,'name': 'Aditya', 'perc': 96},
    'student2': {"rollno": 20,'name': 'Michel','perc': 99},
    'student3': {'rollno': 30, 'name': 'john snow', 'perc': 76}
}

print(students)

# with open('students.json', 'w') as file:
#     json.dump(students,file, indent=4)

# load()
'''
with open('students.json','r') as file:
    data = json.load(file)
print(data)
'''
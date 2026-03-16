# stud1 = {
#     'maths': 80.6,'eng': 76,'phy': 90  }

# # print(stud1['phy'])
# # print(stud1.get('chem'))

# emp1 = {'id': 10012, 'name': 'Aditya', 'salary': 18000}
# # print(emp1.get('phone', 12345678))

# # membership operator

# print('id' in emp1)

# # update dictonary
# emp1['Phone'] = 9964121234
# print(emp1)

# stud1.update(emp1)
# print(stud1)
# ------------------------------------------------------------------

stud1 = {
    'id':1 , 'name': 'aditya', 'age': 23, 'marks': {'English': 45,'Bio': 56,'Chem': 75, 'Maths': 86 } }
# print('chemestry marks',stud1['marks']['Chem'])
# 
# fetch only keys of the dictonary

print(stud1.keys())

# fetch only values
print(stud1.values(),type(stud1.values))

# print is  function 
# predefine code 

# displays the value in outpoot feed

# builtin fun : written by py devs

print('This is the function ')

# def add(*args):
#     print(args)
#     return sum(args)

# a = add(1,2,3,5,6,7,8,6,4,3,4,5,4,3,3,4,3,1)
# print(a)

# student details

# def student_detail(id, name, *marks):
#     if len(marks) == 0:
#          print(f"{name} with id  {id} is absent for the exam\n")
#     else:
#         percentage = sum(marks) / len(marks)
#         print(f"{name} with id  {id} secured {percentage}%\n")


# student_detail(12,'Aditya', 56,78,89,45,76,60.1)
# student_detail(12,'Gunj', 56,78,89,66,76,60.1)
# student_detail(12,'Pravin', 56,78,89,88,76,60.1)
# student_detail(12,'chitrasen')

# vareable lenth keyword argument
# **kwargs = vareable length positional argument(0 to n):
def func(id, name,*extra,**marks):
    if len(marks) == 0:
        print(f"{name} with id  {id} is absent for the exam\n")
    else:

        percent = sum(marks.values()) / len(marks)
        print(f"{name} with id {id} secured {percent}")
        print(f"friends of {name}'s are {extra}")

func(1,"Aditya" ,'CHITRASEN','cj','Gunjan','swapnil',phy = 67,chem = 89, english= 50)
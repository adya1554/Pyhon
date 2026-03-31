# raise 

# salary < 0:
age = int(input('Enter an Salary : '))
if age < 0:
    raise ValueError("age not be less than zero")
else:
    if age > 18:
        print('you can vote')
    else:
        print('you cant vote')
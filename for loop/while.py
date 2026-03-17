# while loop simple example


# n = 1
# while n < 5:
#     print('printing the number : ',n)
#     n = n+1

# while loop reallife example
# login password using while

correct_password  = 'Adya@1554'
while True:
    user_password = input('Password: ') 
    if user_password == correct_password:
        print("Password is Correct")
        print('logged inn')
        break
    else:
        print("Wrong Password, Try Again :)")

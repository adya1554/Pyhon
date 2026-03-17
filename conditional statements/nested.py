# nested if loop
'''
first check is student pass or fail
thendecide the grade

'''
marks = int(input('Enter your Marks = '))
 
if marks >= 50:
    print('YOU PASS THE HARDEST EXAM !!!')

    if marks>=90:
        print("'A' Grade")
    elif marks>=80 and marks<90:
        print("'B' Grade")
    elif marks >=50 and marks<80:
        print("C Grade")
else:
    print('better luck next time !!!')
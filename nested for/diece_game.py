"""
write a program to simulate a roll a die/diece
A diece has 6 faces with numbers 1 t 6 written on them
The program should randomly print an number
"""

import random
print('Welcome to the Luck Game')
while True:
    choice = input("Press 'Enter' to roll the diece or 'q' to Quit the game : ")
    if choice =='q':
        print("thanks for playing a Game , Byee :)")
        break
    elif choice == "":
        number = random.randint(1,6)
        print(f"\n\nYour number ia {number}")
        print(f"you can move {number} step Ahed\n\n")
    else:
        print("\n\nInvalid Input---\n\n")
        
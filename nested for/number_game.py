import random
print('welcome to number guessing game. We have a numbe that need to guessed . \n You have 10 chances\n')
print('The secret number is between 1 to 50')
print('you have 10 Attempts\n\n\t-----Game Start---------')


rand = random.randint(1,50)

isguess = False
for i in range(1,11):
    print(f"You have {11-i} left")
    guess = int(input("Enter your Guess : "))
    if guess == rand :
        print("Congrats Your Guess is correct !!\n")
        isguess = True
        break
    elif guess > rand: 
        print('Your Guess is Lower ! Try Again :)\n')
    elif guess < rand :
        print('Your Guess is Higher ! Try Again \n')
    else:
        print("BETTER LUCK NEXT TIME !!")

if isguess == False:
    print('Bad Luck!! you exasted all your attempts and coudent guess the number.')
print(f"The secret number was {rand}. Game Over")

    


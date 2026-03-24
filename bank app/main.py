def check_balance():
    print(f"Balance : {bal}")
    print("Thank You")

def withdrown():
    withdrown_amout = int(input("Enter the amount to withdrown : "))
    if withdrown_amout > bal:
        print("Insuficeant BALANCE")
    else:
        bal -= withdrown_amout
        print(f"Withdrown Amount : {withdrown_amout}")
        print(f"Balance : {bal}")
        print("Thank You")


def diposit():
    pass

# main.py

print("Welcome To NeoBank")
bal = 2530
while True:
    print('\t1. Check Balance\n\t2. Withdrow Money\n\t3. Diposit\n\t4. Exit\n\n')
    choice = input("Enter Your choice : ")
    if choice == '1':
        check_balance()
    elif choice == '2':
        withdrowng()
    elif choice == '3':
        diposit()
    elif choice == '4':
        break
    else:
        print("Invalid Input Re-try")
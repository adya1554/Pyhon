def factorail(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorail(num-1)
        
        
n = int(input('Enter an NUmber : '))
res = factorail(n)
print(f"factorial of {n} : {res}")
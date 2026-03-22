# recursion - a process that call itself until condition not get satisfy 
# Factorial - of n = n*n-1, n-1*n-2

# 4! = 4 * 3 * 2 * 1 = 24


number = int(input('enter an Number - '))
fact = 1
while number > 1:
    fact = fact * number
    number = number - 1
print(fact)
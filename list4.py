# Remove duplicates from a list.
list2 = [1,2,3,4,5,6,6,6,6,6,7,8]
a = set(list2)
# print(type(a))
print(f"Actual list before delting    : {list2}")
print(f"after deleting duplicate items:{a}")

# Find the second-largest number.
list2 = [1,2,3,4,5,6,6,6,6,6,7,8,23,45,1,3,4,5,6,7,3,567,444,100]
a = set(list2)
b=sorted(a)
print(b)
print(f"second largest number is : {b[-2]}")
    
list2 = [1,2,3,4,5,6,6,6,6,6,7,8,23,45,1,3,4,5,6,7,3,567,444,100]
n = int(input("Enter an Number :"))
print(f"the {n} number apears in list {list2.count(n)}")


list2 = [1,2,3,4,5,6,6,6,6,6,7,8,23,45,1,3,4,5,6,7,3,567,444,100]
n = int(input("Enter an Number :"))
number = 0
for i in list2:
    if i == n:
        number =number+1
        
print(number)   


# Separate a list into even and odd numbers.
list2 = [1,2,3,4,5,6,6,6,6,6,7,8,23,45,1,3,4,5,6,7,3,567,444,100]
even = []
odd  = []
for i in list2:
    if i%2 == 0:
        even.append(i)
        
    else:
        odd.append(i)
        
print(f"Even list: {even}")
print(f"odd list : {odd}")

# tuple similer list 
# comma saparated elements in tuple
# decleard in ()
# sequence of item as collection
print('-------------------------------------------\n\n\n')

t1 = ('python', 'gay',('sam','cj','gunj',0), 10, 3.14, [1,3,'aditya'], ['amit','swapnil'])
print('this is a tuple =', t1)
print('last index of the tuple',t1[-1])
print('last second index tuple',t1[-2])
print('typeof this is -',type(t1),)
print('-------------------------------------------\n\n\n')


t2 = 1,3,5,['aditya','gunjan']
print(t2)
print(type(t2))
print('-------------------------------------------\n\n\n')

l1 = [1,2,3,4,1,2,3,2]
print(l1,type(l1))
t = tuple(l1)
print(t,type(t))
print('-------------------------------------------\n\n\n')
fruits = ('mango', 'orange', 'apple')
print(fruits,type(fruits))

fruits = list(fruits)
print(fruits,type(fruits))
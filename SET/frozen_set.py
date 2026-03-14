# frozen set - frozen set are immutable 

s = {1, 2, 4, 5, 7}
s.add(-1)
print(s)


# to create frozen set 
fset = frozenset({10,20,30})
print(type(fset))

print(fset)

print(fset & fset)
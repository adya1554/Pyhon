seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filterd_op = map(lambda x: True if x % 2 != 0 else False, seq)
print(filterd_op)
print(f"Odd Numbers from the seq are : {list(filterd_op)}")
#  compike time error
#  indentation error

# Exeption => errors during exucution

# use to handle exeption ==>> try-exept block



try:
    with open("D:/Python/file handaling/games",'rt') as fh:
        res = fh.read()

    

except FileNotFoundError as err:
    print("The shoud be present there !!\n")
    print(err)
except ValueError:
    print('Value cant be an charecter')

else:
    print(res)
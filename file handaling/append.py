import os 


with open('D:/python/file handaling/games', 'at') as ff:
    # containt =)
    # ff.write('\nwriten by with statement file close not used')

# print(containt)


filen = 'D:\Python\file handaling\append.py'

if os.path.exists(filen):
    print('path exists')
else:
    print('not exist')

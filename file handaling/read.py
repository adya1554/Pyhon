# # for opening and creating the file
# fh = open("croma1.txt", 'xt')

# # writing into the file
# fh.write('This is file handling \ni am learning \ni am writing this from the read.py file')
# fh.write('\nHello Croma Vegacity')

# for closing the file..

# ----------------------------------------------------------
# wrirting the file
# in writing file it distroy the entire data inside that
# while using take pricoctions

# fuck = open("d:/Python/file handaling/games", 'wt')

# fuck.write('\nstill i have hopes i can crack the job in it')
# fuck.close()

# -----------------------------------------------------------


# read file 
# reading the file and printing on the terminal
fi = open("d:/Python/file handaling/games", 'rt')
contain = fi.read()
line1 = fi.readline()
line2 = fi.readline()
line3 = fi.readline()
# print(f"{line1}\n{line2}\n{line3}")

f1 = open("d:/Python/file handaling/games", 'rt')
lines = f1.readlines()
# print(f"lines : {lines}")
for i in lines:
    print(i.strip())

# print(contain)
f1.close()
try:
    # 1. Open and read the file
    with open("D:\Python\Assinement 4\sample.txt", "r") as file:
        # 2. Print content line by line
        print('\n')
        for line in file:
            print(line.strip())

        print('\n')

except FileNotFoundError:
    # 3. Handle error if file does not exist
    print("Error: sample.txt does not exist.")
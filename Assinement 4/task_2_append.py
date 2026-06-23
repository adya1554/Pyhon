while True:
    str = input('Enter text to write to the file : ')
    with open('Assinement 4/output.txt' ,'at') as fh:
        fh.write(str)
        print("data succusfully written to output.txt")
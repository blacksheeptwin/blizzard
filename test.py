fname = input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        line = line.rstrip()
        line= line.upper()
        print (line)

except:
    print('Enter a valid file name:')
    exit()

print("hey liam")

#trial

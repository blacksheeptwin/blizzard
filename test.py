'''
file = input("Enter file name: ")
fh = open(file)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        line2 = line[20:]
        line3 = float(line2)
        total = total+line3
average = total/count
print("Average spam confidence:",average)
'''
'''
#Assignment 8.4
list2 = list()
file = input ("Enter file name: ")
fh = open(file)

for liam in fh:
    new_list =liam.split()
    for words in new_list:
        if (words not in list2):
            list2.append(words)
list2.sort()

print(list2)
'''
'''
#Assignment 8.5
count = 0
file = input("Enter file name: ")
fh = open(file)
for line in fh:
    line2 = line.rstrip()
    if line2.startswith('From ') :
        newline = line2.split()
        count = count + 1
        print(newline[1])
print ("There were",  count, "lines in the file with From as the first word")
'''
'''
#Assignment 8.4 again

file = input("Enter File Name ")
fh = open(file)
list2 = list()
for line in fh:
    list1 = line.split()
    for x in list1:
        if(x not in list2):
            list2.append(x)
list2.sort()
print(list2)
'''
'''
#Assignment 8.5 again
count = 0
file = input("Enter file name ")
fh = open(file)
for line in fh:
    if(line.startswith('From ')):
        newline = line.split()
        indexline=newline[1]
        count = count + 1
        print(indexline)
print(count)

'''
file = input("Enter File Name ") #Enter file name
fh = open(file) #Open the file
hashtable=dict() #Create a blank dictionary
for line in fh: # Go through each line in the file
    if(line.startswith('From ')):  # If the line start with "from"
        line2=line.split()  #Split the words in each line
        line3= line2[1]  #Take the second word of the line as the sender address
        hashtable[line3] = hashtable.get(line3,0) + 1  # Create histogram hash table
hashkey = None
hashvalue = None
for line3, value in hashtable.items():
        if hashkey is None or value > hashvalue:
            hashkey = line3
            hashvalue = value
print(hashkey, hashvalue)

#hi liam

#Assignment 9.4

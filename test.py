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

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ooba=0
count=0
store=0
imley=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        store=line[20:]
        ooba=float(store)+ooba
        count=count +1
        continue
imley=str(ooba/count)
print('Average spam confidence: '+ imley)

import re
name = input('Enter the file name: ')
file = open(name)
count = 0
sum = 0
for line in file:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    for i in x:
        count = count + 1
        sum = sum + float(i)
print(sum / count)

import re
name = input('Enter the file name: ')
try:
    file = open(name)
except Exception:
    print('Error. File does not exist')
    exit()
exp = input('Enter a regular expression: ')
count = 0
for line in file:
    line = line.rstrip()
    if re.findall(exp, line):
        count = count + 1
print(name, 'had', count, 'lines that matched', exp)

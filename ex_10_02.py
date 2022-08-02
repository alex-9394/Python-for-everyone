name = input('Enter the file name: ')
try:
    file = open(name)
except Exception:
    print('File does not exist')
    exit()
ddd = {}
for line in file:
    line = line.rstrip()
    words = line.split()
    if len(line) < 3 or words[0] != 'From':
        continue
    else:
        word = words[5]
        time = word.split(':')
        hour = time[0]
        ddd[hour] = ddd.get(hour, 0) + 1

lst = sorted([(hour, value) for hour, value in ddd.items()])

for hour, value in lst:
    print(hour, value)

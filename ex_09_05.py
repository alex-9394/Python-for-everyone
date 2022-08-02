name = input('Enter the file name: ')
file = open(name)
ddd = {}
for line in file:
    line = line.rstrip()
    words = line.split()
    if len(line) < 3 or words[0] != 'From':
        continue
    else:
        word = words[1]
        email = word.split('@')
        school = email[1]
        ddd[school] = ddd.get(school, 0) + 1
print(ddd)

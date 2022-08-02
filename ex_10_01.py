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
        ddd[word] = ddd.get(word, 0) + 1

lst = []
for word, value in ddd.items():
    lst.append((value, word))

lst.sort(reverse=True)

for value, word in lst[:1]:
    print(word, value)

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
big_email = None
big_count = None
for word, count in ddd.items():
    if big_count is None or count > big_count:
        big_email = word
        big_count = count
print(big_email, big_count)

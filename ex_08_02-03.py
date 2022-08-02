file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    words = line.split()
    if len(line) < 3 or words[0] != 'From':
        continue
    print(words[2])

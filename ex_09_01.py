file = open('words.txt')
ddd = {}
value = 0
for line in file:
    words = line.split()
    for word in words:
        if word not in ddd:
            value = value + 1
            ddd[word] = value
if 'rewarding' in ddd:
    print('True.', 'Value:', ddd['rewarding'])
else:
    print('False')
print(ddd)

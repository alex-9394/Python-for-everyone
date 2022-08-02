file = open('romeo.txt', 'r')
list = list()
for line in file:
    for word in line.split(' '):
        if word not in list:
            list.append(word.rstrip())
print(sorted(list))

import string
name = input('Enter the file name: ')
try:
    file = open(name)
except Exception:
    print('Error. File does not exist')
    exit()
ddd = dict()

for line in file:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        for letter in word:
            ddd[letter] = ddd.get(letter, 0) + 1

lst = list()
for key, value in ddd.items():
    lst.append((value, key))
lst.sort(reverse=True)
for value, key in lst:
    print(key, value)


file_name = input('Enter the file name ')
try:
    file = open(file_name)
except Exception:
    print('Error. File does not exist')
    quit()
count = 0
for line in file:
    if line.startswith('From:'):
        word = line.split()
        print(word[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')

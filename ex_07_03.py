file_name = input('Enter the file name ')
if file_name == 'monkey.txt':
    print('Got you XD')
    quit()
try:
    file = open(file_name)
except Exception:
    print('Error. File does not exist')
    quit()
count = 0
sum = 0.0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        a = line.find(':')
        b = line.find(' ', a + 2)
        c = float(line[a + 2:b])
        sum = sum + c
        count = count + 1
print('Average spam confidence:', sum / count)

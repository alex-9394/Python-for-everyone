count = 0
total = 0.0
while True:
    n = input('Enter a number: ')
    if n == 'done':
        break
    try:
        number = float(n)
    except Exception:
        print('Bad input')
        continue
    count = count + 1
    total = total + number
print(count, total, total / count)
input('Press ENTER to quit')

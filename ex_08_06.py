list = []
while True:
    n = input('Enter a number: ')
    if n == 'done':
        break
    try:
        number = float(n)
        list.append(number)
    except Exception:
        print('Bad input')
        continue
print("Maximum: ", max(list))
print("Minimum: ", min(list))
input('Press ENTER to quit')

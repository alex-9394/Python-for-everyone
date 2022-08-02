hours = input('Enter hours ')
rate = input('Enter rate ')
fh = float(hours)
fr = float(rate)
if fh <= 40:
    pay = fh * fr
    print('You earned', pay, 'euros this week')
else:
    pay = 40 * fr + (fh - 40) * 1.5 * fr
    overtime = fh - 40
    print('You worked', overtime, 'hours overtime')
    print('You earned', pay, 'euros this week')
input('Press ENTER to exit')

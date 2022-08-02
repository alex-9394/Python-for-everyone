def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        pay = hours * rate
    return pay


h = input('Enter hours ')
r = input('Enter rate ')
fh = float(h)
fr = float(r)

pay = computepay(fh, fr)

print('You earned', pay, 'euros this week')
input('Press ENTER to exit')

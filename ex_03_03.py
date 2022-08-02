score = input('What is your score?\n')
try:
    fs = float(score)
    if fs < 0 or fs > 1:
        print('Error. Enter a number from 0 to 1.0')
    if fs >= 0 and fs < 0.6:
        print('F')
    elif fs >= 0 and fs <= 0.69:
        print('D')
    elif fs >= 0 and fs <= 0.79:
        print('C')
    elif fs >= 0 and fs <= 0.89:
        print('B')
    elif fs >= 0 and fs <= 1:
        print('A')
except Exception:
    print('Bad input')
    quit()
quit()

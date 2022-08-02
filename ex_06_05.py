sentence = 'adewqeqweiqwp: 0.056'
n = sentence.find(':')
number = float(sentence[n + 2:])
print(number)

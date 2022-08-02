import urllib.request
url = input('Enter URL: ')
file = urllib.request.urlopen(url).read()
file = file.decode()

print(file[:3000])
print(len(file))

suma = 0
file = open('numbers.txt','r')
for s in file:
    suma +=int(s)
    print(s)
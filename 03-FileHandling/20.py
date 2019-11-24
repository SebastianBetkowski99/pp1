tab = []
with open('numbers.txt') as file:
    for line in file:
        if int(line) % 2 == 0:
            tab.append(int(line))
with open('evennumbers.txt', 'w+') as file:
    for s in tab:
        file.write(str(s)+'\n')
print(tab)
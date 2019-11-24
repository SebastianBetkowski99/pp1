tab = []
with open("numbers.txt", 'r') as tekst:
    for line in tekst:
        tab.append(int(line))
tab.sort()
for s in tab:
    print(s, end=' ')
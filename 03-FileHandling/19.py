tab= []
with open('universities.txt', 'r') as file:
    for line in file:
        tab.append(line.strip('"'))

tab.sort()

with open('universities.txt', 'w') as file:
    for item in tab:
        file.write(item)
print(tab)
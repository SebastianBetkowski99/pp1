tab =[]
with open('numbersinrows.txt') as file:
    for line in file:
        tab += line.split(',')
tab =[int(s) for s in tab]
print('Ilość liczb: {}\nSuma: {} '.format(len(tab), sum(tab)))
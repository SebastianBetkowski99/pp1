tablica=[32, 16, 5, 8, 24, 7]
file=open('tablica.txt','w')
for s in tablica:
    file.write(str(s)+"\n")
file.close()
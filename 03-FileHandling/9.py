s = 0
with open('NoEducation.txt','r') as file :
    for line in file:
        print(str(s)+" "+line,end='')
        s+=1
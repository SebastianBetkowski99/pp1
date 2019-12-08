import csv
with open('employees.csv', newline='') as s:
 reader=csv.reader(s, delimiter=',')
 count=0
 for row in reader:
     if count==0:
         print("#","\t".join(row))
     count = count +1
     if count==1:
         print("="*30)
     else:
         print("\t".join(row))
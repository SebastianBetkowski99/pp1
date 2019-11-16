file=open('shoppinglist.txt','a')
produkty=input("Podaj nazwe produktu: ")
file.write(str(produkty+"\n"))
file.close()
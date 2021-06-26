import os
os.system("clear")
i = 0
elementos = int( input("quantos elementos = "))
lista = []
while len(lista) < elementos:
    os.system("clear")
    i += 1 
    print(i) 
    elemento = input("elemento ")
    lista.append(elemento)

os.system("clear")
    
for x in lista:
    print(x)


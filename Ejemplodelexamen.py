import random

num_ale = str(random.randrange(10000, 100000))
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_ale)
for n in num_ale:
    doble = num_ale.count(n)
    if doble <= 1:
        print("bien")
    else:
        print("mal")





num = input(str("Introduzca un número de 5 cifras: "))
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = []
if len(num) != 5:
    print("no hay 5 cifras")
for n in num:
    doble = num.count(n)
    if doble <= 1:
        print("bien")
    else:
        print("no vale")
print(num.split(" ", 5))

entrada=input("Introduce una cadena: ")
 
diccionario={}
 
for letra in entrada:
    if letra in diccionario:
        if diccionario > 5:
            print("mal")
    else:
        diccionario[letra]=1
 
print(diccionario)
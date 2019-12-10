num = int(input("Introduzca un número entero positivo: "))
def numperfectos (num):
    suma = 1
    for i in range(2, num):
        if (num % i == 0):
            suma = suma + i
    if (suma == num):
        print("El número",num,"es un número perfecto.")
    else:
        print("El número",num,"no es un número perfecto.")

for i in range (0, num):
    lista = []
    list.append(lista)
    print(numperfectos(num))
    break
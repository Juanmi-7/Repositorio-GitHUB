# Crear una función que calcule la suma de la progresión geométrica: 1 + x + x2 + x3 + . . . + xn:
import math
print("Función de la suma de la siguiente progresión geométrica:")

def calcularprogresion (n, x):
    calculo = 0
    for i in range (0, n):
        calculo += x**i
    return(calculo)

if __name__=="__main__":
    n = int(input("Introduzca un valor para n: "))
    x = int(input("Introduzca un valor para x: "))
    print("El resultado de la suma de la progresión geométrica es de:", calcularprogresion (n, x))
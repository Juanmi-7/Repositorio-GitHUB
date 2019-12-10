# Crear una función que calcule la distancia entre dos puntos en el plano.
import math
print("Función de la distancia entre dos puntos de un plano:")

def distanciaentredospuntos ():
    print("Introduzca los valores de la coordenada 1:")
    x1 = int(input("Introduzca el valor de x1: "))
    y1 = int(input("Introduzca el valor de y1: "))
    print("Introduzca los valores de la coordenada 2:")
    x2 = int(input("Introduzca el valor de x2: "))
    y2 = int(input("Introduzca el valor de y2: "))
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("La distancia entre los puntos 1 y 2 es de:", round(distancia, 4))

distanciaentredospuntos ()
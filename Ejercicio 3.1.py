# Crear un programa que calcule las raíces de un polinomio de segundo grado del tipo: ax2 + bx +c
import math

a = int(input("Introduzca un valor: "))
b = int(input("Introduzca un valor: "))
c = int(input("Introduzca un valor: "))
d = b**2 - 4*a*c

if d < 0:
    print ("No existe solución para esta ecuación.")
elif d == 0:
    x = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    print("Esta ecuación tiene una sola solución: ", x)
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    print("Esta ecuación tiene dos soluciones: ", x1, "y", x2)
# Crear una función denominada eliminar_extremos que reciba una lista y elimine el primer y el último elemento de la misma.
# Usar la función para crear un programa que calcule la puntuación media de la valoración de 8 jueces eliminando los valores máximo y mínimo.

def eliminar_extremos(lista):

    lista.pop(0)
    lista.pop(len(lista1) - 1)
    return lista

def eliminar_mayor_menor(lista):

    ordenada = lista.sort()
    lista.pop(0)
    lista.pop(len(lista) - 1)
    return lista

def media(lista):

    suma = 0
    for i in lista:
        suma = suma + i
    media = suma / len(lista)
    return media

lista = [5, 2, 9, 4, 1, 6, 7, 8]
lista1 = [5, 56, 54, 432, 2, 4, 45]
print(eliminar_extremos(lista1))
print(eliminar_mayor_menor(lista))
print("La puntuación media es de:", media(lista))
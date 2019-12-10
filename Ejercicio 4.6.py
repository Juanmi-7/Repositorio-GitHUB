# Crear una función denominada hay_duplicados que reciba una lista y devuelva True si contiene duplicados o False si no es así.
# Usar la función para generar una lista de 20 números aleatorios del 1 al 100 que no contenga duplicados.
import random

def hay_duplicados(numero, lista):

    if lista.count(numero) > 0:
        return True
    else:
        return False

def aleatorios(lista1):

    while len(lista1) < 20: 
        n = random.randint(1, 101)
        if hay_duplicados(n, lista1) == True:
            continue
        lista1.append(n)
    return lista1

lista1 = []
print(aleatorios(lista1), len(lista1))
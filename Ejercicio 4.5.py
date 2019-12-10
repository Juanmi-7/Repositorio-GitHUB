# Crear una función denominada en_orden_ascendente que reciba una lista y devuelva True si se encuentra ordenada en orden ascendente o False si no es así.
# Crear otra función denominada esta_ordenada que reciba también una lista y devuelva True si se encuentra ordenada (ascendente o descendente) y False si no es así. Intenta hacerlo sin tener que recorrer la lista dos veces.

def en_orden_ascendente(lista):

    if lista == lista.sort:
        return True
    else:
        return False

def esta_ordenada(lista):

    if lista == lista.sort or lista == lista.sort(reverse=True):
        return True
    else:
        return False

lista = [3, 5, 7, 1, 4, 2, 6]
print(en_orden_ascendente(lista))
print(esta_ordenada(lista))
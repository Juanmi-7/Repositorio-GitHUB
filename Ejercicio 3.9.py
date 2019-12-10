# Crear una función que devuelva el número de dígitos necesarios para expresar un número en binario.

def num_digitos(numero):
    binario = bin(numero)
    len(binario)
    return len(binario) - 2

numero = int(input("Introduzca un número: "))
print("El número de dígitos necesarios para expresar el número introducido en binario es: ", num_digitos(numero))
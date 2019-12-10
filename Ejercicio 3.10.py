# Crear un programa para jugar a adivinar un número entre 0 y 100. Debe ofrecer cinco oportunidades e indicar ante un fallo si el objetivo es menor, mayor o esta muy cerca (a 2 de distancia o menos). Se debe utilizar una función para comprobar si el número es el acertado o no y hacer las indicaciones al jugador.

import random

def numero_aleatorio ():

    num_ale = int(random.randrange(0, 101))
    return num_ale

num_ale = numero_aleatorio()
oportunidades = 5
while True:
    try:
        numero = int(input("Introduzca un número del 0 al 100: "))
        if numero == num_ale:
            print("Has acertado!")
            break
        elif numero > 100 or numero < 0:
            print("Por favor, introduzca un número del 0 al 100.")
        elif numero > num_ale:
            oportunidades = oportunidades -1
            dif1 = numero - num_ale
            if dif1 <= 2:
                print("Está muy cerca del número!")
                print("Te quedan", oportunidades, "oportunidades.")
            else:
                print("Te quedan", oportunidades, "oportunidades.")
        elif numero < num_ale:
            oportunidades = oportunidades -1
            dif2 = num_ale - numero
            if dif2 <= 2:
                print("Está muy cerca del número!")
                print("Te quedan", oportunidades, "oportunidades.")
            else:
                print("Te quedan", oportunidades, "oportunidades.")
        else:
            print("Fallo.")
        if oportunidades == 0:
            print("Has perdido.")
            break
    except ValueError:
        print("Por favor, introduzca un número.")
import random
palabras = ["cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana"]
resultado = []
fallos = 5
aciertos = 0
contador = 0
palabra = list(random.choice(palabras))
while fallos > 0:
    letra = input(str("\nIntroduzca una letra: ")).lower()
    try:
        if letra in palabra and letra not in resultado:
            resultado.append(letra)
            contador += palabra.count(letra)
            print("\nBien! Hay", palabra.count(letra), letra,":")
            for i in palabra:
                if i in resultado:
                    print(i, end = " ")
                    del i
                else:
                    print("_", end = " ")
            if len(palabra) == contador:
                print("\nEnhorabuena, has acertado!")
                break
        else:
            print("\nOooops, fallo.")
            fallos -= 1
            print("Te quedan", fallos, "intentos.")
    except ValueError:
        print("Por favor, introduzca una letra.")
else:
    print("Lo siento, has perdido.")
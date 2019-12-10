import random

def numero_aleatorio (num_ale):

    num_ale = str(random.randrange(10000, 100000))
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in num_ale:
        doble = num_ale.count(n)
        if doble <= 1:
            return True
        else:
            return False

def comprueba (num):

    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    muertos = []
    heridos = []
    intentos = 0

    if len(num) != 5:
        print("Ese número no tiene 5 cifras.")
    
    for n in num:
        doble = num.count(n)
        if doble <= 1:
            return True
        else:
            return False

    try:
        if n in num and n in num_ale:
            intentos += num_ale.count(n)
            print("Hay", muertos.count(n),"muertos y", heridos.count(n), "heridos.")
            for n in num_ale:
                if n in resultado:
                    print(n, end = " ")
                    del n
                else:
                    print("_", end = " ")
            if num_ale.count(n == 5):
                print("Enhorabuena, has acertado en", intentos, "intentos.")
    except:
        print("hio")

numero_aleatorio
num = input(str("Introduzca un número de 5 cifras: "))
print(numero_aleatorio)
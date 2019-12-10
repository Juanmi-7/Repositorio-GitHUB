# Crear una función que devuelva si un año es bisiesto.

def añobisiesto ():
    año = int(input("Introduzca un año: "))

    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("El año", año,"es bisiesto")
            else:
                print("El año", año, "no es bisiesto")
        else:
            print("El año", año, "es bisiesto.")
    else:
        print("El año", año, "no es bisiesto.")

añobisiesto ()
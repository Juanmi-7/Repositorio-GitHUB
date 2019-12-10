# Crear una función que devuelva si una fecha es válida reutilizando la función del ejercicio 3.6.

def añobisiesto (año):

    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def diames (dia, mes, año):

    if dia>0 and dia<32 and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        return True
    else:
        return False
    if dia>0 and dia<31 and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        return True
    else:
        return False
# añobisiesto(año)

a = int(input("Introducir un año: "))
b = int(input("Introducir un día: "))
c = input("Introducir un mes: ")
if diames (b, c, a) == True:
    print("La fecha introducida es correcta.")
elif añobisiesto (a) == True:
    if b>0 and b<30 and c == "febrero":
        print("La fecha introducida es correcta.")
    else:
        print("La fecha introducida es incorrecta.")
elif añobisiesto (a) == False:
    if b>0 and b<29 and c == "febrero":
        print("La fecha introducida es correcta.")
    else:
        print("La fecha introducida es incorrecta.")
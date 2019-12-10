# Usar las funciones de los ejercicios 3.6 y 3.7 para reescribir el ejercicio 2.24.

from datetime import datetime

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

    if dia > 0 and dia < 32 and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        return True
    else:
        return False
    if dia > 0 and dia < 31 and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        return True
    else:
        return False
    if añobisiesto (año) == True:
        if dia > 0 and dia < 30 and mes == "febrero":
            return True
        else:
            return False
    else:
        if dia > 0 and dia < 29 and mes == "febrero":
            return True
        else:
            return False

def mayor20 (dia, mes, año):

    formato1 = "%d/%m/%Y"
    nacim = str(dia)+"/"+str(mes)+"/"+str(año)
    actual = datetime.now()
    formato2 = actual.strftime("%d/%m/%Y")
    actual = datetime.strptime(formato2, formato1)
    nacim = datetime.strptime(nacim, formato1)
    if actual >= nacim:
        dif = actual - nacim
        if dif.days >= 7305:
            return True
        elif dif.days < 7305:
            return False

a = int(input("Introducir su año de nacimiento: "))
b = int(input("Introducir el día que nació: "))
c = input("Introducir el mes en el que nació: ")
cnum = 0

if c == "enero":
    cnum = 1
elif c == "febrero":
    cnum = 2
elif c == "marzo":
    cnum = 3
elif c == "abril":
    cnum = 4
elif c == "mayo":
    cnum = 5
elif c == "junio":
    cnum = 6
elif c == "julio":
    cnum = 7
elif c == "agosto":
    cnum = 8
elif c == "septiembre":
    cnum = 9
elif c == "octubre":
    cnum = 10
elif c == "noviembre":
    cnum = 11
elif c == "diciembre":
    cnum = 12

if diames (b, c, a) == True:
    print("La fecha introducida es correcta.")
else:
    print("La fecha introducida es incorrecta.")

if mayor20 (b, cnum, a) == True:
    print("Usted es mayor de 20 años.")
else:
    print("Usted es menor de 20 años.")
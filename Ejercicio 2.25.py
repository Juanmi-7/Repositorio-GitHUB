from datetime import datetime
from datetime import timedelta
formato = "%d/%m/%Y"
fecha = input("Introduzca una fecha (dd/mm/aaaa): ")
fecha2 = input("Introduzca el día 1 de Enero de ese año (dd/mm/aaaa): ")
fecha = datetime.strptime(fecha, formato)
fecha2 = datetime.strptime(fecha2, formato)
dia = input("Introduzca el día de la semana en que cayó el 1 de Enero de ese año: ")
semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
posicionactual = semana.index(dia)
dif = fecha - fecha2
m = (dif.days)
n = m % 7
diaactual = semana[(posicionactual + n) % 7]
print("El día de la semana correspondiente a la fecha introducida es",diaactual)
#for x in semana:
#    n = (m % 7 + semana.index(dia))%7
#while True:
#    print(n)
#    if n == 0:
#        print("El día de la semana correspondiente a la fecha introducida es Lunes.")
#        break
#    elif n == 1:
#        print("El día de la semana correspondiente a la fecha introducida es Martes.")
#        break
#    elif n == 2:
#        print("El día de la semana correspondiente a la fecha introducida es Miércoles.")
#        break
#    elif n == 3:
#        print("El día de la semana correspondiente a la fecha introducida es Jueves.")
#        break
#    elif n == 4:
#        print("El día de la semana correspondiente a la fecha introducida es Viernes.")
#        break
#    elif n == 5:
#        print("El día de la semana correspondiente a la fecha introducida es Sábado.")
#        break
#    elif n == 6:
#        print("El día de la semana correspondiente a la fecha introducida es Domingo.")
#        break
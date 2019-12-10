import calendar
year = int(input("Introduzca un año: "))
month = int(input("Introduzca un mes del año: "))
calendario = calendar.Calendar()
for elemento in calendario.monthdayscalendar(year, month):
    print(elemento)
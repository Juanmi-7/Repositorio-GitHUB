try:
    a=int(input("número: "))
    if not a%400 or (not a%4 and a%100):
        print("si")
    else:
        print("no")
except:
    print("no es numero")

# Los resultados son: 2000 = si; 2010 = no; 2012 = si; 2100 = no. El programa comprueba las condiciones (numero divible entre 400 o numero divisible entre 4 y 100) y luego imprime el texto en las que se cumplan.
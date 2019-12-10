try:
    a=int(input("número: "))
    p=True
    for n in range(2,a):
        if not a%n:
            p=False
            break
    if p:
        print("si")
    else:
        print("no")
except:
    print("no es numero")

# Los resultados son: 3 = si; 8 = no; 13 = si. El programa divide el número introducido entre todos los números desde el 2 al número introducido. Si el número es divisible entre alguno de ellos, la solución es False (no). En caso contrario la solución es True (sí).
try:
    n=int(input("numero: "))
except:
    n=3
a=1
for i in range(n,0,-1):
    print(" "*i+"*"*a)
    a+=2
print(" "*(n-1)+"*"*3)

# Los resultados son filas de *, empezando con un * en la primera fila y sumando 2 * en la línea siguiente (uno al inicio de fila y otro al final de la misma), hasta llegar a la última fila, en la que se muestran 3 * centrados. En el caso de que se introduzca un valor erróneo, el programa tomará el valor 3.
def binarizar(dec):
    bin = ""
    while dec // 2 != 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return str(dec) + bin
num = int(input("Introduzca un número decimal para convertirlo a binario: "))
print(binarizar(num))
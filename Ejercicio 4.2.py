texto = input("Introduce una texto: ")
cantidad = {}
for letra in texto:
    if letra in cantidad:
        cantidad[letra] = cantidad[letra] + 1
    else:
        cantidad[letra] = 1
print(cantidad)
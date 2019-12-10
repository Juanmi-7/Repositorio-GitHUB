# Intento 1:
cadena = input("Introduzca un texto: ")
ocurrencias = cadena.count("")
print(ocurrencias)

# Intento 2:
cadena1 = input("Intrduzca un texto: ")
cadena2 = len(cadena1)
print(cadena2)

# Intento 3:
entrada=input("Introduce una texto: ")
diccionario={}
for letra in entrada:
    if letra in diccionario:
        diccionario[letra]=diccionario[letra]+1
    else:
        diccionario[letra]=1
print(diccionario)

# Intento 4:
texto = str(input("introduzca el texto: ")).lower()
vyc = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
lista = []
for nv in texto:
    if nv not in vyc:
        lista.append(nv)
texto_sin_vocales = "".join(lista)
print(texto_sin_vocales)

# Intento 5:
texto = str(input("introduzca el texto: ")).lower()
vyc = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
num = [0, 27]
for letra in vyc:
    texto = texto.replace(vyc, (num, vyc))
print(texto)
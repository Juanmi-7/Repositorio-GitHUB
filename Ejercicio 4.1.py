texto = input("Introduzca el texto: ").lower()
texto1 = texto2 = texto
vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")
for letra in vocales:
    texto = texto.replace(letra, "")
print(texto)

consonantes = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
for letra in consonantes:
    texto1 = texto1.replace(letra, "")
print(texto1)

tex1 = texto2.replace("a", "A")
tex2 = tex1.replace("e", "E")
tex3 = tex2.replace("i", "I")
tex4 = tex3.replace("o", "O")
tex5 = tex4.replace("u", "U")
tex6 = tex5.replace("á", "Á")
tex7 = tex6.replace("é", "É")
tex8 = tex7.replace("í", "Í")
tex9 = tex8.replace("ó", "Ó")
tex10 = tex9.replace("ú", "Ú")
print(tex10)
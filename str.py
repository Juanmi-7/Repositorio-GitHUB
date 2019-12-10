s = "hola"
str(s)
print(s)
s = 'Hola mundo.'
str(s)
'Hola mundo.'
repr(s)
"'Hola mundo.'"
str(1.0/7.0)
'0.142857142857'
repr(1.0/7.0)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '...'
print(s)
# El valor de x es 32.5, y es 40000...
# El repr() de una cadena agrega apóstrofos y barras invertidas
hola = 'hola mundo\n'
holas = repr(hola)
print(holas)
'hola mundo\n'
# El argumento de repr() puede ser cualquier objeto Python:
repr((x, y, ('carne', 'huevos')))
"(32.5, 40000, ('carne', 'huevos'))"
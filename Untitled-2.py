print("Puntuación\tCalificación")
print(">= 0.9\t\tSobresaliente")
print(">= 0.8\t\tNotable")
print(">= 0.7\t\tBien")
print(">= 0.6\t\tSuficiente")
print("< 0.6\t\tInsuficiente")
try:
    nota = float(input("Introduce la nota que has sacado : "))
    if nota >= 0.9:
        print("Has sacado un sobresaliente")
    elif nota >= 0.8:
        print("Has sacado un notable")
    elif nota >= 0.7:
        print("Has sacado un bien")
    elif nota >= 0.6:
        print("Has sacado un suficiente")
    else:
        print("Estás suspenso")
except ValueError:
    print("Mete un valor válido")
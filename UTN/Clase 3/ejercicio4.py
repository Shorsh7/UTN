# Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido.

edad = int(input("Ingresá tu edad: "))

print("Has cumplido años: ")

for año in range(1, edad + 1):
    print(año)


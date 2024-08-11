# Ejercicio 4:
# Escriba un programa que solicite el radio de una circunferencia y permita calcular el área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# 𝐴 = 𝜋. 𝑟2
# A = Área 
# π = Número pi igual a 3.1416
# r = Radio

radio = float(input("Ingresá el radio de la circunsferencia: "))
PI = 3.1416
area = PI ** radio

print("Área:", area)
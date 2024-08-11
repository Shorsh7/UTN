# Realice nuevamente los ejercicios de la Unidad 1 (3, 4 y 5), pero tratando de utilizar una función, de forma que la operación se realice dentro de si misma.
# Presente el resultado en la terminal del editor.

# Ejercicio 4:
# Escriba un programa que solicite el radio de una circunferencia y permita calcular el área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula: 𝐴 = 𝜋. 𝑟2
# A = Área 
# π = Número pi igual a 3.1416
# r = Radio

PI = 3.1416

def longitud(radio):
    area = PI * (radio ** 2)
    print("El área según el radio es: ", area)

radio_ingresado = int(input("Ingrese el radio: "))
longitud(radio_ingresado)




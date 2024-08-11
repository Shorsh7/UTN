# Realice nuevamente los ejercicios de la Unidad 1 (3, 4 y 5), pero tratando de utilizar una función, de forma que la operación se realice dentro de si misma.
# Presente el resultado en la terminal del editor.

# Ejercicio 3:
# Escriba un programa que solicite el perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula: L = 2 · π · r
# L = Longitud de perímetro
# π = Número pí igual a 3.1416
# r = Radio

PI = 3.1416

def longitud(radio):
    perimetro = 2 * PI * radio
    print("El perímetro según el radio es: ", perimetro)

radio = (int(input("Indique el radio: ")))
longitud(radio)


# Realice nuevamente los ejercicios de la Unidad 1 (3, 4 y 5), pero tratando de utilizar una función, de forma que la operación se realice dentro de si misma.
# Presente el resultado en la terminal del editor.

# Ejercicio 5:
# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal del editor el valor incrementado en un 10%.

def incrementar_valor():
    valor = int(input("Ingrese un valor entero: "))
    
    valor_incrementado = valor * 1.10
    
    print(f"El valor incrementado en un 10% es: ", valor_incrementado)

incrementar_valor()
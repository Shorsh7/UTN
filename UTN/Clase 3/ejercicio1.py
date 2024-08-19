# Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo.

import sys

print(sys.argv)

"""
['ejercicio1.py', '10', '15']
"""

print("Si el valor de dividir por 2 da resto 0, entonces es par. Si no, es impar.")

for valor in range(1, len(sys.argv)):
    numero = int(sys.argv[valor])
    resto = numero % 2
    if resto == 0:
        tipo = "par"
    else:
        tipo = "impar"
    
    print(f"El número que ingresaste es: {numero}. El resto de dividir por 2 es: {resto}. Por lo tanto, es {tipo}.")
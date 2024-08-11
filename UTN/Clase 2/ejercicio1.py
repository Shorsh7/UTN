import sys

# Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan pasar tres parámetros.
# El programa debe tomar los parámetros e indicar en la termina si son múltiplos de dos.
# UTILICE LA ESTRUCTURA IF/ELSE.

print(sys.argv)

"""
['ejercicio1.py', '12', '25', '38']
"""

variable_1 = int(input("Ingrese un parámetro: "))
variable_2 = int(input("Ingrese un nuevo parámetro: "))
variable_3 = int(input("Ingrese un tercer parámetro: "))

variable_1 = int(sys.argv[1])
variable_2 = int(sys.argv[2])
variable_3 = int(sys.argv[3])

def es_multiplo_de_dos(numero):
    if numero % 2 == 0:
        return f"{numero} es múltiplo de dos."
    else:
        return f"{numero} no es múltiplo de dos."

print(es_multiplo_de_dos(variable_1))
print(es_multiplo_de_dos(variable_2))
print(es_multiplo_de_dos(variable_3))


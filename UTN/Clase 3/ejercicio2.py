# Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”.

oracion = input("Ingresá una oración aleatoria: ")

indice = 0
total_letra_a = 0

while indice < len(oracion):
    if oracion[indice] == "a":
        total_letra_a += 1
    indice += 1

print(f"La letra 'a' aparece en la oración una cantidad de {total_letra_a} veces.")


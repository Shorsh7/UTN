# Escriba un programa que consulte al usuario por una oración y comente al usuario 
# cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.

oracion = input("Ingresá una oración aleatoria: ")

vocales = {
    'a': 0, 'A': 0, 'á': 0, 'Á': 0,
    'e': 0, 'E': 0, 'é': 0, 'É': 0,
    'i': 0, 'I': 0, 'í': 0, 'Í': 0,
    'o': 0, 'O': 0, 'ó': 0, 'Ó': 0,
    'u': 0, 'U': 0, 'ú': 0, 'Ú': 0
}

for letra in oracion:
    if letra in vocales:
        vocales[letra] += 1

print(f"La cantidad de vocales en tu oración es de {vocales}.")
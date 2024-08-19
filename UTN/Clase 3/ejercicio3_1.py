# Escriba un programa que consulte al usuario por una oración y comente al usuario 
# cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.

oracion = input ("Por favor escribí una oración: ").lower()

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú",
           "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]

for vocal in vocales:
    cantidad = oracion.count(vocal)
    if cantidad > 0:
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")
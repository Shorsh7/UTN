# A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.

seleccion = input("Para comenzar, ingresá 'c', para finalizar, ingresá 'f': ")

total = 0
compras = []

if seleccion == 'c':
    valor = True
else:
    valor = False

while valor == True:
    producto, cantidad, precio = input("Ingresá el nombre y la cantidad del producto en kilos y el precio, separados por espacios: ").split()
    total = total + float(cantidad) * float(precio)

    compras.append((producto, float(cantidad), float(precio)))

    seleccion = input("Para agregar otro producto, seleccioná 'a', para finalizar, seleccionar otro caracter: ")
    if seleccion == 'a':
        valor = True
    else:
        valor = False

print(compras)
print("El valor total de la compra es de: ", total)

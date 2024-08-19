# Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. 
# Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado.

seleccion = input("Para comenzar, ingresá 'c', para finalizar, ingresá 'f': ")

total = 0

if seleccion == 'c':
    valor = True
else:
    valor = False

while valor == True:
    producto, cantidad, precio = input("Ingresá el nombre y la cantidad del producto en kilos y el precio, separados por espacios: ").split()
    total = total + float(cantidad) * float(precio)
    seleccion = input("Para agregar otro producto, seleccioná 'a', para finalizar, seleccionar otro caracter: ")
    if seleccion == 'a':
        valor = True
    else:
        valor = False

print("El valor total de la compra es de: ", total)
# A partir del ejerció 7 cree un programa con 4 funciones:
# alta() para dar de alta la nueva compra.
# baja() para dar de baja una compra.
# consulta() para consultar por todas las compras realizadas hasta el momento.
# modificar() para modificar una compra realizada.

total = 0
compras = {}

def alta():
    global total
    producto, cantidad, precio = input("Ingresá el nombre y la cantidad del producto en kilos y el precio, separados por espacios: ").split()
    cantidad = float(cantidad)
    precio = float(precio)
    total += cantidad * precio
    compras[producto] = {
        "Cantidad": cantidad,
        "Precio por KG": precio
    }
    print(f"Producto '{producto}' añadido correctamente.")

def baja():
    global total
    producto = input("Ingresá el nombre del producto que deseas eliminar: ")
    if producto in compras:
        total -= compras[producto]["Cantidad"] * compras[producto]["Precio por KG"]
        del compras[producto]
        print(f"Producto '{producto}' eliminado correctamente.")
    else:
        print(f"Producto '{producto}' no encontrado.")

def consulta():
    print("Compras realizadas:")
    for producto, detalles in compras.items():
        print(f"{producto}: {detalles['Cantidad']} kg a ${detalles['Precio por KG']} por kg")
    print(f"El valor total de la compra es de: ${total}")

def modificar():
    global total
    producto = input("Ingresá el nombre del producto que deseas modificar: ")
    if producto in compras:
        nueva_cantidad, nuevo_precio = map(float, input("Ingresá la nueva cantidad y el nuevo precio, separados por espacios: ").split())
        total -= compras[producto]["Cantidad"] * compras[producto]["Precio por KG"]
        compras[producto] = {
            "Cantidad": nueva_cantidad,
            "Precio por KG": nuevo_precio
        }
        total += nueva_cantidad * nuevo_precio
        print(f"Producto '{producto}' modificado correctamente.")
    else:
        print(f"Producto '{producto}' no encontrado.")

seleccion = input("Para comenzar, ingresá 'c', para finalizar, ingresá 'f': ")
if seleccion == 'c':
    valor = True
else:
    valor = False

while valor:
    accion = input("Seleccioná una acción: alta (a), baja (b), consulta (c), modificar (m), finalizar (f): ").lower()
    
    if accion == 'a':
        alta()
    elif accion == 'b':
        baja()
    elif accion == 'c':
        consulta()
    elif accion == 'm':
        modificar()
    elif accion == 'f':
        valor = False
    else:
        print("Opción no válida. Por favor, seleccioná una acción válida.")

print("Programa finalizado.")

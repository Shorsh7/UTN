# A partir del ejerció 6 cree un programa con 4 funciones:
# alta() para dar de alta la nueva compra,
# baja() para dar de baja una compra,
# consulta() para consultar por todas las compras realizadas hasta el momento,
# modificar() para modificar una compra realizada.

lista_de_compras = []

def alta(compra):
    lista_de_compras.append(compra)
    print(f"Se agregó {compra} a tu lista de compras.")

def baja():
    lista_de_compras.clear()
    print("Se vació tu carrito.")

def consulta(compra):
    if len(lista_de_compras) > 0:
        print(f"Productos en tu carrito: {lista_de_compras}")
    else:
        print("Tu carrito está vacío.")

def modificar_compra():

    if len(lista_de_compras) > 0:
        print("En tu carrito hay:")
        for indice, valor in enumerate(lista_de_compras):
            print(f"{indice}: {valor}")

        indice_modificar = input("Ingresá el índice del elemento que querés modificar: ")
                
        if indice_modificar.isdigit():
            indice_modificar = int(indice_modificar)

            if 0 <= indice_modificar < len(lista_de_compras):
                nuevo_valor = input("Ingresá el nuevo valor: ")

                lista_de_compras[indice_modificar] = nuevo_valor

                print("Tu nueva lista tiene:")
                for indice, valor in enumerate(lista_de_compras):
                    print(f"{indice}: {valor}")
            else:
                print("Índice inexistente. No se realizó ninguna modificación.")
        else:
            print("Debes ingresar un número válido.")
    else:
        print("Tu carrito está vacío, no hay nada para modificar.")

def menu ():
     while True:
        opcion = input("Hola, bienvenido/a al sistema de compras de la verdulería. ¿Qué querés hacer hoy?\n"
                       "1. Hacer una compra\n"
                       "2. Vaciar el carrito\n"
                       "3. Consultar tu carrito\n"
                       "4. Modificar tu carrito\n"
                       "5. Salir\n"
                       "Selecciona una opción (1-5): ")
        if opcion == '1':
            compra = input("Ingrese el nombre del producto a agregar: ")
            alta(compra)
        elif opcion == '2':
            baja()
        elif opcion == '3':
            consulta(compra)
        elif opcion == '4':
            modificar_compra()
        elif opcion == '5':
            print("Gracias por usar el sistema de compras de la verdulería. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor ingrese un número del 1 al 5.")

menu()



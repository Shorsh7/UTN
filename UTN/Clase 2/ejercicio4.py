# Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
# fecha de jubilación, presente en la terminal el mensaje
# caso contrario que presente "Aún está en edad de trabajar."

EDAD_JUBILACION_HOMBRE = 65
EDAD_JUBILACION_MUJER = 60

edad = int(input("Por favor, ingrese su edad: "))

genero = input("Por favor, ingrese su género (M para masculino, F para femenino): ").upper()

if genero == "M":
    if edad >= EDAD_JUBILACION_HOMBRE:
        print("Ya está en edad de jubilación.")
    else:
        print("Aún está en edad de trabajar.")
elif genero == "F":
    if edad >= EDAD_JUBILACION_MUJER:
        print("Ya está en edad de jubilación.")
    else:
        print("Aún está en edad de trabajar.")
else:
    print("Género no válido. Por favor, ingrese M para masculino o F para femenino.")

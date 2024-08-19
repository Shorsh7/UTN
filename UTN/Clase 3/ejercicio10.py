# Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que esta sea correcta. 
# El programa debe informar al usuario si la contraseña fue correcta o no.  

contraseña = "elcodeoesmipasion"

entrada = ""

while entrada != contraseña:
    entrada = input("Por favor, ingrese la contraseña: ")
    
    if entrada == contraseña:
        print("¡Contraseña correcta! Bienvenido al sistema.")
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
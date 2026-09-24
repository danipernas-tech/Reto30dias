#Crea un programa que simule un sistema básico de acceso mediante contraseña.
contraseña = "holaDani123"
contraseña_user = input("Introduce la contraseña: ")
intentos = 1
while True:
    if contraseña != contraseña_user:
        print ("Contraseña incorrecta")
        if intentos == 1:
            print("Inténtalo de nuevo")
        elif intentos == 2:
            print("ültimo intento")
        else:
            print("Cuenta bloqueada")
            break
        contraseña_user = input("Introduce la contraseña: ")
        intentos += 1
    else:
        print("Acceso concedido")
        print(f"Intentos: {intentos}")
        break

constraseña = "hola1234"
user_contraseña = input("Introduce la contraseña: ")

intentos = 0
while user_contraseña != constraseña:
    print("Error: contraseña incorrecta")
    intentos += 1
    if intentos == 1:
        print("Inténtalo de nuevo")
    elif intentos == 2:
        print("Último intento")
    elif intentos == 3:
        print("Cuenta bloqueada")
        break
    user_contraseña = input("Introduce la contraseña: ")
    
print(f"\nBienvenido al sistema, has necesitado {intentos} intentos.")

while True:
    print("---- GENERADOR DE PATRONES ----")
    caracter = input("\n¿Que caracter quieres utilizar?: ")
    print("\nElige el PATRON:")
    print("1. Rectángulo")
    print("2. Triangulo normal")
    print("3. Triangulo invertido")
    print("4. Salir")
    opcion = int(input("\n"))

    if opcion == 1:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        for i in range (filas):
            print(caracter * columnas)
    elif opcion == 2:
        altura = int(input("Introduce la altura: "))
        for i in range (altura + 1):
            print(caracter * i)
    elif opcion == 3:
        altura = int(input("Introduce la altura: "))
        for i in range (altura, 0, -1):
            print(caracter * i)
    elif opcion == 4:
        break



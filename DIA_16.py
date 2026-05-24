import random
mapa = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ]

fila_tesoro = random.randint(1, 8)
columna_tesoro = random.randint(1, 8)
intentos = 0

for i in mapa:
        print(" ".join(i))

while True:

    fila_user = int(input("Dime en que fila esta el tesoro: "))
    columna_user = int(input("Dime en que columna esta el tesoro: "))

    intentos += 1

    if fila_user < 1 or fila_user > 8 or columna_user < 1 or columna_user > 8:
        print("Coordenadas no válidas")
        continue

    if fila_user == fila_tesoro and columna_user == columna_tesoro:
        mapa[fila_tesoro][columna_tesoro] = "X"
        for i in mapa:
            print(" ".join(i))
        print("\nHas encontrado el tesoro")
        print(f"Intentos: {intentos}")
        break
    else:
        print("No has encontrado el tesoro")
        if fila_user > fila_tesoro:
            print("El tesoro está más arriba")
        elif fila_user < fila_tesoro:
            print("El tesoro está más abajo")
        if columna_user > columna_tesoro:
            print("El tesoro está más a la izquierda")
        elif columna_user < columna_tesoro:
            print("El tesoro está más a la derecha")

    '''
    if columna_user >= 1 and columna_user <=8 and fila_user >= 1 and fila_user <= 8:
        for i in range (1, fila_user + 1):
            for j in range (1, columna_user + 1):
                if i == fila_tesoro and j == columna_tesoro:
                    mapa[fila_tesoro][columna_tesoro] = "X"
                    for i in mapa:
                        print(" ".join(i))
                    break
                else: 
                    print("No has encontrado el tesero")
                    if fila_user > fila_tesoro:
                        print("El tesoro está más arriba")
                    elif fila_user < fila_tesoro:
                        print("El tesoro está más abajo")
                    if columna_user > columna_tesoro:
                        print("El tesoro está más a la izquierda")
                    elif columna_user < columna_tesoro:
                        print("El tesoro está más a la derecha")
    '''
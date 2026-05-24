import random
tablero = [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
]

barco = [(2, 3), (2, 4), (2, 5)] 
intentos = 0

for i in tablero:
    print(" ".join(i))

while True:
    disparo_fila = int(input("A que fila quieres disparar: "))
    disparo_columna = int(input("A que columna quieres disparar: "))

    intentos += 1

    if (disparo_fila, disparo_columna) == barco[0] or (disparo_fila, disparo_columna) == barco[1] or (disparo_fila, disparo_columna) == barco[2]:
        tablero[disparo_fila - 1][disparo_columna - 1] ="X"
        print("Tocado")
    else:
        tablero[disparo_fila - 1][disparo_columna - 1] = "0"
        print("Agua")
    
    for i in tablero:
        print(" ".join(i))
    
    
    if tablero[barco[0][0] -1][barco[0][1] - 1] == "X" and tablero[barco[1][0] - 1][barco[1][1] - 1] == "X" and tablero[barco[2][0] - 1][barco[2][1] - 1] == "X":
        print("¡Tocado y hundido!")
        break


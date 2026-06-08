import random

numeros = random.sample(range(1, 31), 15)
numeros_contador = 0

carton = []
linea = 0

for i in range (3):
    fila = []
    for j in range (5):
        numero = numeros [numeros_contador]
        fila.append(numero)
        numeros_contador += 1
    carton.append(fila)

print("--- CARTON ---")
for i in carton:
    print(i)

input("\nPresiona Enter para empezar el Bingo")


bolas = random.sample(range(1, 31), 30)
bolas_contador = 0
for i in range (30):
    bola = bolas[bolas_contador]
    print(f"\nBola: {bola}")
    for i in range (3):
        for j in range (5):
            if carton [i][j] == bola:
                carton [i][j] = "X"
                print("Has acertado!")
    print("\n--- CARTON ACTUALIZADO ---")
    for i in carton:
        print(i)
    bolas_contador += 1
    for i in range (3):
        if carton[i][0] == "X" and carton[i][1] == "X" and carton[i][2] == "X" and carton[i][3] == "X" and carton[i][4] == "X" and      linea == 0:
            linea = 1
            print("\nLINEA!")
    lineas_marcadas = 0
    for i in range (3):
        if carton[i][0] == "X" and carton[i][1] == "X" and carton[i][2] == "X" and carton[i][3] == "X" and carton[i][4] == "X":
            lineas_marcadas += 1
    if lineas_marcadas == 3:
        print("\nBINGO!!!!")
        break
    input("\nPresiona Enter para seguir")

    


    
    
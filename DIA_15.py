

while True:
    jugadores = int(input("Cuántos jugadores participan?: "))
    if jugadores >= 2:

        for i in range (1, jugadores + 1):
            for j in range (i + 1, jugadores + 1):
                print(f"Jugador {i} vs Jugador {j}")
        break
    else:
        print("Necesitas mas jugadores")

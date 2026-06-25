
mapas = {
    "Nuketown": 0,
    "Raid": 0,
    "Hijacked": 0,
    "Standoff": 0
}

mayor = -1
mapa_elegido = ""

print("Mapas disponibles: ")
for clave in mapas.keys():
    print(f"- {clave}")

jugadores = int(input("\nCuántos jugadores van a votar?: "))

print()
for i in range (jugadores):
    while True:
        voto = input(f"Jugador {i + 1} a que mapa quieres votar?: ")
        if voto in mapas:
            mapas[voto] += 1
            break
        else:
            print("Mapa no valido")

print("\n--- RESULTADOS ---")
for clave, valor in mapas.items():
    print(f"{clave} -> {mapas[clave]} votos")
    
for clave, valor in mapas.items():
        if valor > mayor:
            mayor = valor
            mapa_elegido = clave 

print(f"\nMapa elegido:  {mapa_elegido}")









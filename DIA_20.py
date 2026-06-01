numero_canciones = int(input("Cuántas canciones quieres añadir?: "))
canciones = []

for i in range (numero_canciones):
    cancion = input(f"Canción {i+1}: ")
    canciones.append(cancion)

mostrar = int(input("\nSi quieres ver la playlist pulsa 1: "))
if mostrar == 1:
    print("\n--- PLAYLIST ---")
    for i in range(numero_canciones):
        print(f"Cancion {i+1}: {canciones[i]}")

posicion = int(input("\nQue posición quieres consultar?: "))
if posicion <= len(canciones) and posicion > 0:
    print(f"La canción de la posición {posicion} es: {canciones[posicion-1]}")
else:
    print("No hay una canción en esa posición")

nombre = input("\nQue canción quieres buscar: ")
for i in range(len(canciones)):
    if nombre.lower() == canciones[i].lower():
        print("La canción existe en la Playlist")
        print(f"Posición: {i+1}")
        break

else:
    print("Canción no encontrada")






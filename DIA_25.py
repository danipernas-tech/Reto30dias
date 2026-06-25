import random

cartas = ["Caballero", "Arquera", "Mago", "Gigante", "Dragón", "Bruja", "Príncipe"]
coleccion = {}

def abrir_sobre():
    sobre = random.choices(cartas, k=5)
    for i in sobre:
        if i in coleccion:
            coleccion[i] += 1
        


while True:
    print("--- APERTURA DE SOBRES ---")
    print("1. Abrir sobre")
    print("2. Ver colección")
    print("3. Consultar carta")
    print("4. Ver estadísticas")
    print("5. Salir")
    opcion = input("Que opción eliges?: ")
    match opcion:
        case "1":
            abrir_sobre()
    
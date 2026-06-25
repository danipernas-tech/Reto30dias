
personajes = []

def crear_personaje():
    personaje_dic = {
        "nombre": "",
        "vida": 0,
        "ataque": 0,
        "defensa": 0
    }
    personaje_dic["nombre"] = input("\nDime el nombre del personaje: ")
    personaje_dic["vida"] = int(input("Dime sus puntos de vida: "))
    personaje_dic["ataque"] = int(input("Dime sus puntos de ataque: "))
    personaje_dic["defensa"] = int(input("Dime sus puntos de defensa: "))
    personajes.append(personaje_dic)
    
def ver_personajes():
    print("\n--- PERSONAJES ---")
    posicion = 1
    if len(personajes) > 0:
        for i in personajes:
            print(f"{posicion}. Nombre: {i["nombre"]}")
            print(f"Vida: {i["vida"]}")
            print(f"Ataque: {i["ataque"]}")
            print(f"Defensa: {i["defensa"]}")
            posicion += 1
    else:
        print("\nNo se ha creado ningún personaje")

              
def buscar_personaje():
    personaje = input("\nQue personaje quieres buscar: ")
    existe = False
    for i in personajes:
        if personaje == i["nombre"]:
            existe = True
            print(f"Nombre: {i["nombre"]}")
            print(f"Vida: {i["vida"]}")
            print(f"Ataque: {i["ataque"]}")
            print(f"Defensa: {i["defensa"]}")
            break
    if existe == False:
        print("\nNo esta ese personaje")
    

while True:
    print("\n--- CREADOR DE PERSONAJES ---")
    print("1. Crear personaje")
    print("2. Ver personajes")
    print("3. Buscar personaje")
    print("4. Salir")
    opcion = input("\nQue opción eliges: ")
    match opcion:
        case "1":
            crear_personaje()
        case "2":
            ver_personajes()
        case "3":
            buscar_personaje()
        case "4":
            print("\nFin del creador de personajes")
            break
        case _:
            print("\nOpción no valida")



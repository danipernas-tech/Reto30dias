import random

mochila = []
objetos = ["pocion", "espada", "escudo", "llave", "moneda", "mapa", "antorcha", "llave dorada", "gema antigua", "pergamino magico"]
contador = 0

def opcion1():
    global contador
    objeto_aleatorio = random.choice(objetos)
    print(f"\nHas encontrado: {objeto_aleatorio}")
    
    if 5 > len(mochila):
        if objeto_aleatorio in mochila:
            print("Ya tienes este objeto")
        else:
            mochila.append(objeto_aleatorio)
            print("Objeto añadido a la mochila")
            contador += 1
    else:
        print("La mochila está llena y no puedes guardarlo")
    if "llave dorada" in mochila and "gema antigua"in mochila and "pergamino magico" in mochila:
        print("Has completado la misión secreta: tienes llave dorada, gema antigua y pergamino mágico")


def opcion2():
    objeto_usar = input("Dime el nombre del objeto que quieres usar: ").lower()
    if objeto_usar in mochila:
        mochila.remove(objeto_usar)
        print(f"Has usado {objeto_usar} y se ha eliminado de la mochila")
    else:
        print("No tienes ese objeto en la mochila")

def opcion3():
    print("\n--- MOCHILA ---")
    if 0 == len(mochila):
        print("Mochila vacia")
    else:
        for i in range (len(mochila)):
            print(f"{i + 1}. {mochila[i]}")

def opcion4():
    objeto_buscar = input("Qué objeto quieres buscar en la mochila: ").lower()
    if objeto_buscar in mochila:
        print(f"Si tienes este objeto: {objeto_buscar}")
    else:
        print("No tienes ese objeto en la mochila")

def opcion5():
    global contador
    print("Fin de la aventura")
    print(f"Has encontrado {contador} objetos")



while True:
    print("\n--- MOCHILA DEL AVENTURERO ---")
    print("1. Encontrar objeto")
    print("2. Usar objeto")
    print("3. Ver mochila")
    print("4. Buscar objeto")
    print("5. Salir")
    opcion = input("\nQue opción eliges: ")
    match opcion:
        case "1":
            opcion1()
        case "2":
            opcion2()
        case "3":
            opcion3()
        case "4":
            opcion4()
        case "5":
            opcion5()
            break
        case _:
            print("Opción no válida, volviendo al menu")
    
        






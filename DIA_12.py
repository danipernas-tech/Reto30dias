
import random
saldo = 10
simbolos = ["🍒", "🍋", "⭐", "🔔"]
resultado = []
partidas = 0
victorias = 0 

while True:
    print("---- TRAGAPERRAS ----")
    print(f"\nSaldo actual: {saldo} monedas")
    print(f"\n1. Jugar partida")
    print(f"2. Añadir saldo")
    print(f"3. Ver saldo")
    print(f"4. Salir")
    opcion = int(input("\nElige opción: "))
    
    if opcion == 1:
        if saldo >= 1:
            saldo -= 1
            resultado = random.choices(simbolos, k=3)
            if resultado == ["⭐", "⭐", "⭐"]:
                print("JACKPOT!!!")
                saldo += 25
                victorias += 1
            elif resultado[0] == resultado[1] == resultado [2]:
                saldo += 10
                print("PREMIO GORDO!")
                victorias += 1
            elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
                saldo += 3
                print("PREMIO")
                victorias += 1
            print(f"Resultado: {resultado}")
            print(f"Saldo actual: {saldo}")
        else:
            print(f"\nSaldo insuficiente!")
            continue
        partidas += 1
    elif opcion == 2:
        añadido = int(input("¿Cuántas monedas quieres añadir?: "))
        if añadido > 0:
            saldo += añadido
            print(f"Se han añadido {añadido} a tu saldo")
        else:
            print("No se permite esa cantidad")
            continue
    elif opcion == 3:
        print(f"Tu saldo actual es de {saldo} monedas")
    elif opcion == 4:
        print("\n--- FIN DEL JUEGO ---")
        print(f"Partidas jugadas: {partidas}")
        print(f"Partidas ganadas: {victorias}")
        print("Saliendo del juego...") 
        break
    else:
        print("Opción inválida, volviendo al menú")
        continue







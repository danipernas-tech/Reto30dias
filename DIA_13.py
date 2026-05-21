
import random
dia = 1
while True:
    print("-- Elige la dificultad del juego --")
    print("1. Facil")
    print("2. Normal")
    print("3. Difícil")
    dificultad = int(input("\nIntroduce dificultad: "))
    if dificultad == 1:
        oxigeno = 120
        comida = 100
        energia = 80
        break
    elif dificultad == 2:
        oxigeno = 100
        comida = 80
        energia = 60
        break
    elif dificultad == 3:
        oxigeno = 80
        comida = 60
        energia = 40
        break   
    else: 
        print("Opcion no valida")


while True:
    print(f"---- DIA {dia} ----")
    print("1. Buscar comida")
    print("2. Reparar sistema de oxígeno")
    print("3. Descansar")
    opcion = int(input(""))
    dia += 1
    
    if opcion == 1:
        comida += 20
        energia -= 15
        oxigeno -= 5
        print("Has encntrado suministros de comida")
    elif opcion == 2: 
        energia -= 20
        oxigeno += 10
        comida -= 5
        print("Has reparado parte del sistema de oxígeno")
    elif opcion == 3:
        energia += 15
        comida -= 10
        oxigeno -= 5
        print("Has descansado y recuperado energía")
    num_aleatorio = random.randint(1, 4)
    if num_aleatorio == 1:
        oxigeno -= 15
        print("Ha habido fuga de oxigeno")
    elif num_aleatorio == 2:
        energia += 10
        print("Los paneles solares han cargado tu enegía")
    elif num_aleatorio == 3:
        comida += 15
        print("Has encontrado suministros extras")
    elif num_aleatorio == 4:
        print("No ha ocurrido ningún incidente")
    oxigeno -= 10
    comida -= 10
    energia -= 5
    print("Consumo diario aplicado")
    
    if oxigeno <= 0 or comida <= 0 or energia <= 0:
        print("No has sobrevivido, la nave se ha quedado sin recursos")
        break

    if dia == 7:
        print("¡Has sobrevivido hasta la llegada del rescate!")
        break


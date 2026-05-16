import random

coche_1 = input("Dime el nombre del coche 1: ")
coche_2 = input("\nDime el nombre del coche 2: ")
tiempo_total_coche_1 = 0
tiempo_total_coche_2 = 0
tiempo_coche_1 = 0
tiempo_coche_2 = 0
tiempo_vuelta = 0
victorias_coche_1 = 0
victorias_coche_2 = 0

def vuelta (coche):
    tiempo_vuelta = random.randint(20, 40)
    print(f"{coche}: {tiempo_vuelta}")
    return tiempo_vuelta

for i in range (1, 6):
    print(f"\n--- VUELTA {i} ---")

    tiempo_coche_1 = vuelta(coche_1)
    tiempo_total_coche_1 += tiempo_coche_1
    tiempo_coche_2 = vuelta(coche_2)
    tiempo_total_coche_2 += tiempo_coche_2

    if tiempo_coche_1 < tiempo_coche_2:
        victorias_coche_1 += 1
        print(f"\n{coche_1} ha sido más rápido esta vuelta")
    elif tiempo_coche_2 < tiempo_coche_1:
        victorias_coche_2 += 1
        print(f"\n{coche_2} ha sido más rápido esta vuelta")
    else:
        print(f"\nEmpate en esta vuelta")

print("\n--- RESULTADO FINAL ---")
print(f"\nTiempo total {coche_1}: {tiempo_total_coche_1} segundos")
print(f"\nTiempo total {coche_2}: {tiempo_total_coche_2} segundos")
if tiempo_total_coche_1 < tiempo_total_coche_2:
    print(f"\nGANADOR: {coche_1}")
elif tiempo_total_coche_2 < tiempo_total_coche_1:
    print(f"\nGANADOR: {coche_2}")
else:
    print(f"\nEMPATE")
print(f"\nEl {coche_1} ha ganado {victorias_coche_1} vueltas")
print(f"El {coche_2} ha ganado {victorias_coche_2} vueltas")

    
    

    





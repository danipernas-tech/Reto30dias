
for i in range (1, 6):
    if i == 3:
        continue
    print(i)

suma = 0
while True:
    try:
        val = int(input("Introduce un número (0 para terminar): "))
        if val == 0:
            break
        suma += val
    except ValueError:
        print("Introduce un número valido")
print(f"Suma total: {suma}")



filas = int(input("Dime el número de filas "))
columnas = int(input("Dime el número de columnas: "))

fila_especial = int(input("Dime la filas especial: "))
columna_especial = int(input("Dime la columna especial: "))

for i in range (1, filas + 1):
    for j in range (1, columnas + 1):
        if (fila_especial,columna_especial) == (i, j):
            print (f"  X  ", end=" ")
        else:
            print (f"({i},{j})", end=" ")
    print()


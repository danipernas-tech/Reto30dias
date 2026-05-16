
#Objetivo: combinar bucles, acumuladores y procesamiento de varios datos

total_notas = 0
suma = 0
media = 0
nota_baja = None
nota_mayor = None
aprobados = 0
suspensos = 0
while True:
    nota = float(input("Dime una nota (-1 para terminar): "))
    if nota == -1:
        break
    if nota < 0 or nota > 10:
        print("Nota incorrecta")
        continue
    suma += nota
    total_notas += 1
    if nota_mayor is None or nota > nota_mayor:
        nota_mayor = nota
    if nota_baja is None or nota < nota_baja:
        nota_baja = nota
    if nota >= 5:
        aprobados += 1
    else:
        suspensos += 1    

print("\n---- RESULTADOS ----")
print(f"\nMedia: {suma/total_notas:.2f} ")
print(f"Nota mas alta: {nota_mayor:.2f}")
print(f"Nota mas baja: {nota_baja:.2f}")
print(f"Total de notas: {total_notas}")
print(f"Notas aprobadas: {aprobados}")
print(f"Notas suspensas: {suspensos}")
if suma/total_notas >= 8:
    print("Grupo excelente")
elif suma/total_notas >= 5:
    print("Grupo aceptable")
else:
    print("Grupo mejorable")
print(f"Porcentaje aprobados: {aprobados/total_notas*100:.2f}%")






numero01 = int(input("Dime un número entero: "))
numero02 = int(input("Dime otro número entero: "))

num_mayor = 0
num_menor = 0
son_iguales = "Son iguales"


if numero01 > numero02:
    num_mayor = numero01
    num_menor = numero02
    print(f"Numero mayor: {num_mayor}")
    print(f"Numero menor: {num_menor}")
elif numero02 > numero01:
    num_mayor = numero02
    num_menor = numero01
    print(f"Numero mayor: {num_mayor}")
    print(f"Numero menor: {num_menor}")
else:
    son_iguales = True
    print("Son iguales")

print(f"Suma: {numero01 + numero02}")
print(f"Diferencia: {numero01 - numero02}")

def analizar(numero):
    if numero > 0:
        positivo_negativo = "positivo"
    elif numero == 0:
        positivo_negativo = "igual que 0"
    else:
        positivo_negativo = "negativo"
    if numero % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "impar"
    return positivo_negativo, par_impar

numero01_01, numero01_02 = analizar(numero01)
numero02_01, numero02_02 = analizar(numero02)

print(f"El número {numero01} es {numero01_01} y es {numero01_02}")
print(f"El número {numero02} es {numero02_01} y es {numero02_02}")








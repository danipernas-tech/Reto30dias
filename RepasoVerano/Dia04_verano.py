
numero01 = int(input("Dime un número entero: "))
numero02 = int(input("Dime otro número entero: "))

num_mayor = 0
num_menor = 0
son_iguales = "Son iguales"


if numero01 > numero02:
    num_mayor = numero01
    num_menor = numero02
elif numero02 > numero01:
    num_mayor = numero02
    num_menor = numero01
else:
    son_iguales = True

suma = numero01 + numero02
diferencia = numero01 - numero02

def analizar(numero):
    if numero >






num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

num_mayor = 0
num_menor = 0
son_iguales = False

if num1 > num2:
    num_mayor = num1
    num_menor = num2
elif num2 > num1:
    num_mayor = num2
    num_menor = num1
else:
    son_iguales = True

suma = num1 + num2
diferencia = num_mayor - num_menor

def analizar(num):
    if num > 0:
        pos_neg = "Positivo"
    elif num < 0:
        pos_neg = "Negativo"
    else:
        pos_neg = "Cero"

    if num % 2 == 0:
        par_impar = "Par"
    else:
        par_impar = "Impar"

    return pos_neg, par_impar
num1_pos_neg, num1_par_impar = analizar(num1)
num2_pos_neg, num2_par_impar = analizar(num2)
    

print("\n----- RESULTADOS -----")
if son_iguales:
    print(f"\nLos dos números son iguales ({num1})")
else:
    print(f"\nNúmero mayor: {num_mayor}")
    print(f"Número menor: {num_menor}")
print(f"\nSuma: {suma}")
print(f"Diferencia: {diferencia}")
print(f"\nNúmero 1:")
print(f"- {num1_pos_neg}")
print(f"- {num1_par_impar}")
print(f"\nNúmero 2:")
print(f"- {num2_pos_neg}")
print(f"- {num2_par_impar}")
print("\n----------------------")




nombre = input("¿Cómo te llamas?: ")
nota = float(input("¿Qué nota has sacado?: "))

if nota < 5:
    resultado = "Suspenso"
elif nota <= 6.99:
    resultado = "Aprobado"
elif nota <= 8.99:
    resultado = "Notable"
else:
    resultado = "Sobresaliente"

print(f"Alumno: {nombre}")
print(f"Nota: {nota:.2f}")
print(f"Resultado: {resultado}")
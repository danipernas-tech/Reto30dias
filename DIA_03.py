
nombre = input("Dime tu nombre: ")
nota = float(input("¿Qué nota has sacado?: "))

calificacion = ""
mensaje = ""

if nota < 0 or nota > 10:
    print("Nota no válida")
else:
    if nota < 5:
        calificacion = "Suspenso"
        mensaje = "Hay que seguir mejorando"
    else:
        mensaje = "Buen trabajo"
        if nota <= 6:
            calificacion = "Aprobado"
        elif nota <= 8:
            calificacion = "Notable"
        else:
            calificacion = "Sobresaliente"
    print(f"Alumno: {nombre}")
    print(f"Nota: {nota}")
    print(f"Resultado: {calificacion}")
    print(mensaje)

'''
print(f"Alumno: {nombre}")
print(f"Nota: {nota}")
print(f"Resultado: {calificacion}")
print(mensaje)
'''
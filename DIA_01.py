
nombre = input("Dime tu nombre: ")
año_nacimiento = int(input("Dime tu año de nacimiento: "))
ciudad = input("Ciudad actual en la que vives: ")
año_actual = 2026

nombre[0].upper()

print("----- FICHA DE USUARIO -----")
print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")
print(f"Edad aproximada: {año_actual - año_nacimiento} años")
if(año_actual - año_nacimiento < 30):
    print("Eres joven")
else:
    print("Eres adulto")    
print("----------------------------")
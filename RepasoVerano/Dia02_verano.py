
print("Bienvenido a la tienda")
producto = input("\n¿Qué producto quieres comprar?: ")
precio = float(input("¿Qué precio vas a pagar por unidad?: "))
cantidad = int(input("¿Cuántas unidades vas a comprar?: "))

iva = 0.21
subtotal = cantidad * precio
iva_total = subtotal * iva
total =  iva_total + subtotal
print("\n--- TICKET ---")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unidad: {precio:.2f}€")
print(f"Subtotal: {subtotal:.2f}€")
print(f"IVA: {iva_total:.2f}€")
print(f"TOTAL: {total:.2f}€")

if total >= 20:
    print("Compra grande")
else:
    print("Compra pequeña")



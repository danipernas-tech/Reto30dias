
producto = input("Dime el nombre del producto: ")
precio_ud = float(input("Dime el precio del producto: "))
cantidad = int(input("Dime la cantidad que quieres comprar del producto: "))

iva = 0.21
precio_final = (iva * (precio_ud * cantidad)) + (precio_ud * cantidad)

print("------ TICKET ------")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: {precio_ud}€")
print(f"Subtotal: {cantidad * precio_ud}€")
print(f"IVA (21%): {iva * (precio_ud * cantidad)}€")
print(f"Total: {precio_final}€")
if precio_final < 20:
    print("Compra pequeña")
else:
    print("Compra grande")
print("--------------------")
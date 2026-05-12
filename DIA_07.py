
total_compra = 0
print("--- Bienvenido al Supermercado ---")
productos = []
inicio = int(input("Pulsa el numero 1 para empezar a comprar: "))
while inicio == 1:
    producto = input("Introduce el nombre del producto: " )
    productos.append(producto)
    precio = float(input("Introduce el precio de este producto: "))
    while precio < 0:
        print("No se permiten precios negativos, vuelve a introducir el precio")
        precio = float(input("Introduce el precio de este producto"))
    total_compra += precio
    print(f"Total de tu carrito: {total_compra}€")
    inicio = int(input("Si quieres añadir mas producto pulsa 1, 0 para finzaliza la compra: "))

print(f"\n----RESUMEN PEDIDO----")
print(f"A pagar: {total_compra}")
print(f"Ticket: {productos}")
    




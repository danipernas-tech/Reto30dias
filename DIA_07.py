
total_compra = 0
print("--- Bienvenido al Supermercado ---")
productos = []
total_compra = 0
descuento_10 = 0.10
descuento_20 = 0.20

while True:
    print("\n1. Añadir producto")
    print("2. Ver total actual")
    print("3. Aplicar descuento")
    print("4. Finalizar Compra")
    print("5. Vaciar compra")
    inicio = int(input("\nQue opción eliges: "))
    if inicio <= 5 and inicio > 0:
        if inicio == 1:
            producto = input("\nIntroduce el nombre del prodcuto: ")
            productos.append(producto)
            precio = float(input(f"Introduce el precio de {producto}: "))
            while precio < 0:
                print("No se permiten números negativos, vuelve a introducir el precio: ")
                precio = float(input(f"Introduce el precio de {producto}: "))
            total_compra += precio
        elif inicio == 2:
         print(f"\nEl total del carrito es {total_compra:.2f}€")
         print(f"Productos: {productos}")
        elif inicio == 3:
            if total_compra >= 100:
                print("\nTienes un descuento del 20%!")
                total_compra = total_compra - (total_compra * descuento_20)
                print(f"Carrito: {total_compra:.2f}€")
            elif total_compra >= 50:
                print("\nTienes un descuento del 20%!")
                total_compra = total_compra - (total_compra * descuento_10)
                print(f"Carrito: {total_compra:.2f}€")
            else:
                print("\nNo hay descuento disponible")
                print(f"Carrito: {total_compra:.2f}€")
        elif inicio == 4:
            print(f"\nCompra total: {total_compra}")
            print(f"Productos: {productos}")
            break
        elif inicio == 5:
            total_compra = 0
            print(f"\nCarrito: {total_compra}€")
    else:
        print("\nOpción incorrecta, repite tu respuesta.")







'''
inicio = int(input("Pulsa el numero 1 para empezar a comprar: "))
while inicio == 1:
    producto = input("Introduce el nombre del producto: " )
    productos.append(producto)
    precio = float(input("Introduce el precio de este producto: "))
    while precio < 0:
        print("No se permiten precios negativos, vuelve a introducir el precio")
        precio = float(input("Introduce el precio de este producto"))
    total_compra += precio
    print(f"Total de tu carrito: {total_compra:.2f}€")
    inicio = int(input("Si quieres añadir mas producto pulsa 1, 0 para finzaliza la compra: "))

print(f"\n----RESUMEN PEDIDO----")
print(f"A pagar: {total_compra:.2f}")
print(f"Ticket: {productos}")
'''




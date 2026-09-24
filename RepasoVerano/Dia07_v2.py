lista_compra = {}
total_acumulado = 0
cantidad_10 = 50
cantidad_20 = 100
descuento_porcentaje_10 = 10
descuento_porcentaje_20 = 20
descuento_aplicado = 0

while True:
    print("--- SUPERMERCADO ---\n")
    print("1. Añadir producto\n" \
    "2. Ver total actual\n" \
    "3. Aplicar descuento\n" \
    "4. Finalizar compra\n")
    while True:
        try:
            opcion = int(input("Escoge una opción del menú: "))
            break
        except ValueError:
            print("Introduce un valor correcto para interactuar con el menú")

    match opcion:
        case 1: 
            producto = input("Introduce el productro que quieras añadir: ")
            while True:
                try:
                    precio = float(input("Introduce el precio del producto: "))
                    while precio < 0:
                        print("El precio no puede ser negativo")
                        precio = float(input("Introduce el precio del producto: "))
                    break
                except ValueError:
                    print("Valor de precio incorrecto")
            lista_compra[producto] = precio
            total_acumulado += precio
            print(f"Total acumulado: {total_acumulado:.2f}")
        case 2: 
            print(f"Total acumulado: {total_acumulado:.2f}")
        case 3: 
            if total_acumulado >= cantidad_20:
                descuento_20 = total_acumulado * (descuento_porcentaje_20 / 100)
                total_descuento = total_acumulado - descuento_20
                print(f"Tu precio con descuento del 20% actualmente es: {total_descuento:.2f}")
                print("Finaliza la compra para aplicar el descuento")
                descuento_aplicado = 20
            elif total_acumulado >= cantidad_10:
                descuento_10 = total_acumulado * (descuento_porcentaje_10 / 100)
                total_descuento = total_acumulado - descuento_10
                print(f"Tu precio con descuento del 10% actualmente es: {total_descuento:.2f}")
                print("Finaliza la compra para aplicar el descuento")
                descuento_aplicado = 10
            else:
                print("No se puede aplicar ningún descuento")
        case 4:
            total_final = total_acumulado * (1 - descuento_aplicado / 100)
            print(f"Total antes del descuento: {total_acumulado:.2f}")
            print(f"Descuento aplicado: {descuento_aplicado}%")
            print(f"Precio final de la compra: {total_final:.2f}")
            break


    
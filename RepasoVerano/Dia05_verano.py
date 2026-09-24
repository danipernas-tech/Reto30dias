
precio_compra = float(input("Precio de tu compra: "))
dinero_cliente = float(input("Dinero que vas a entregar: "))
euros = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
precio_compra = int(precio_compra * 100)
dinero_cliente = int(dinero_cliente * 100)
if precio_compra <= dinero_cliente:
    cambio_total = dinero_cliente - precio_compra
    for i in range(len(euros)-1, -1, -1):
        valor = euros[i]
        cantidad = cambio_total // valor
        cambio_total = cambio_total % valor
        if cantidad > 0:
            if valor >= 500:
                print(f"Billetes de {valor / 100} euros: {cantidad}")
            elif valor == 100 or valor == 200:
                    print(f"Monedas de {valor / 100} euros: {cantidad}")
            else:
                print(f"Monedas de {valor} céntimos: {cantidad}")
else:
    print("No tienes dinero suficiente para pagar")


    
 

    

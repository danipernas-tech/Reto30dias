
precio_compra = float(input("Dime el precio de compra: "))
dinero_cliente = float(input("¿Cuánto dinero vas a entregar?: "))
cambio = 0

while precio_compra > dinero_cliente:
    print(f"Necesitas pagar más dinero para este producto de {precio_compra}€")
    dinero_cliente = float(input("¿Cuánto dinero vas a entregar?: "))

precio_compra = int (precio_compra * 100)
dinero_cliente = int(dinero_cliente * 100)

cambio = dinero_cliente - precio_compra
cambio_original = float(cambio / 100)

billetes_500 = cambio // 50000
cambio = cambio % 50000

billetes_200 = cambio // 20000
cambio = cambio % 20000

billetes_100 = cambio // 10000
cambio = cambio % 10000

billetes_50 = cambio // 5000
cambio = cambio % 5000

billetes_20 = cambio // 2000
cambio = cambio % 2000

billetes_10 = cambio // 1000
cambio = cambio % 1000

billetes_5 = cambio // 500
cambio = cambio % 500

monedas_2 = cambio // 200
cambio = cambio % 200

monedas_1 = cambio // 100
cambio = cambio % 100

centimos_50 = cambio // 50
cambio = cambio % 50

centimos_20 = cambio // 20
cambio = cambio % 20

centimos_10 = cambio // 10
cambio = cambio % 10

centimos_5 = cambio // 5
cambio = cambio % 5

centimos_2 = cambio // 2
cambio = cambio % 2

centimos_1 = cambio // 1
cambio = cambio % 1

def devolucion (dinero, nombre):
    if dinero > 0:
        print(f"{nombre} : {dinero}")

precio_compra = float(precio_compra / 100)
dinero_cliente = float(dinero_cliente / 100)
print(f"\n------ TICKET COMPRA ------")
print(f"Precio de la compra: {precio_compra}€")
print(f"Dinero entregado: {dinero_cliente}€")
print(f"\nCambio total: {cambio_original}€")
devolucion(billetes_500, "Billetes de 500€:")
devolucion(billetes_200, "Billetes de 200€:")
devolucion(billetes_100, "Billetes de 100€:")
devolucion(billetes_50, "Billetes de 50€:")
devolucion(billetes_20, "Billetes de 20€:")
devolucion(billetes_10, "Billetes de 10€:")
devolucion(billetes_5, "Billetes de 5€:")
devolucion(monedas_2, "Monedas de 2€:")
devolucion(monedas_1, "Monedas de 1€:")
devolucion(centimos_50, "Monedas de 50 céntimos:")
devolucion(centimos_20, "Monedas de 20 céntimos:")
devolucion(centimos_10, "Monedas de 10 céntimos:")
devolucion(centimos_5, "Monedas de 5 céntimos:")
devolucion(centimos_2, "Monedas de 2 céntimos:")
devolucion(centimos_1, "Monedas de 1 céntimos:")











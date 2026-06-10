
inventario = {
    "pocion": 3,
    "espada": 1,
    "escudo": 2
}

def ver_inventario():
    print("\nINVENTARIO:")
    for clave, valor in inventario.items():
        print(f"{clave} -> {valor} unidades")

def consultar_producto():
    producto = input("\nDime el nombre del producto que quieres consultar: ").lower()
    if producto in inventario:
        print(f"{producto}: {inventario[producto]} unidades")
    else:
        print("Ese producto no existe")

def añadir_unidades():
    producto = input("\nEscribe el prodcuto que quieres añadir: ").lower()
    cantidad = int(input("Cuántas unidades quieres añadir?: "))
    if producto in inventario:
        inventario[producto] += cantidad
        print(f"Unidades añadidas a {producto}")
    else:
        inventario[producto] = cantidad
        print("Producto añadido")

def vender_producto():
    producto = input("\nEscribe el prodcuto que quieres vender: ").lower()
    cantidad = int(input("Cuántas unidades quieres vender?: "))
    if producto in inventario:
        if cantidad > inventario[producto]:
            print("No hay suficientes unidades para vender")
        else:
            inventario[producto] -= cantidad
            if inventario[producto] == 0:
                del inventario[producto]
    else:
        print("Ese producto no existe")

def unidades_total():
    cantidad_total = 0
    for valor in inventario.values():
        cantidad_total += valor
    print(f"\nCantidad total: {cantidad_total}")

while True:
    print("\n--- INVENTARIO DEL MERCADER ---")
    print("1. Ver inventario")
    print("2. Consultar producto")
    print("3. Añadir unidades")
    print("4. Vender producto")
    print("5. Mostrar unidades de todo")
    print("6. Salir")
    opcion = input("\nEscoge una opción: ")
    match opcion:
        case "1":
            ver_inventario()
        case "2":
            consultar_producto()
        case "3":
            añadir_unidades()
        case "4":
            vender_producto()
        case "5":
            unidades_total()
        case "6":
            print("Saliendo...")
            break
        case _:
            print("Escoge una opción correcta del menu")
            continue

        
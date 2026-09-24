
def evaluar_division():
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
    except ValueError:
        print("Introduce un dato correcto")
    else:
        print(f"Resultado división: {resultado}")
    finally:
        print("Operación finalizada")

evaluar_division()


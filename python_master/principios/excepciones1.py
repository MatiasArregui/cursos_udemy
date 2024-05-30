try:
    entrada = int(input("Ingresar un numero entero: "))
    print(f"Numero ingresado: {entrada}")
except Exception as error:
    print(f"no ha ingresado un numero,  error: {error}")


cadena_1 = "Hola mundo"
texto = '''Python es un lenguaje de alto nivel de programación interpretado
cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de
programación multiparadigma, ya que soporta parcialmente la orientación a objetos,
programación imperativa y, en menor medida, programación funcional. '''

cadena_rota = 'matias se"fue a comprar ""'

# print(texto)

lista_texto = texto.split()
# print(lista_texto)
matias_nuevo = cadena_rota.title()
# print(matias_nuevo)
def buscador(texto):
    try:
        while True:
            entrada = input("Ingrese el valor a buscar: ").lower()
            cont=0
            buscador = 0
            if entrada == "": break
            while buscador !=-1:
                buscador = texto.lower().find(" "+ entrada +" ", cont)
                if buscador !=-1:
                    cont+=buscador+1
                    print(f"Indice donde se encuentra la palabra {entrada}: {buscador}")
                else:
                    if cont >= 1:
                        print(f"No mas repeticiones de la palabra {entrada}")
                    else:
                        print(f"Esa palabra no se encuentra en el texto")

    except:
        print("Error en el sistema")

buscador(texto)

cadena_nueva = "matias se fue a caminar#$"
cadena_2 = cadena_nueva.strip("#$")
# print(cadena_2)
# print(cadena_nueva)
lista_2 = [x.lower() for x in texto.split()]
# print(lista_2)
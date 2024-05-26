# Empaquetado y desmpaquetado de variables

tupla = (1,2,3)
a, b, c = tupla

cadena = "matias nicolas arregui"
print(*cadena)

def suma(*args):
    total = 0
    for x in args:
        total += x
    return total

sumatoria = suma(1,2,3,4,5)
print(sumatoria)

# Las keys deben ser igual que los nombres de los parametros
def sobre(nombre, edad, pais):
    cadena = f"{nombre} se fue a {pais} a sus {edad} años"
    return cadena

diccionario = {
    "nombre":"matias",
    "edad":25,
    "pais":"Argentina"
}
print(sobre(**diccionario))

def mostrar(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")

mostrar(**diccionario)
mostrar(nombre = "matias", apellido = "arregui", edad = 25)
lista_1 = [1,2,3,4,5]
print(suma(*lista_1))

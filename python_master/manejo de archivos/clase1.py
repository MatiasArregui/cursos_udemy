with open("manejo de archivos\\texto2.txt", "w", encoding="utf-8") as file:
    file.write("hola mundo")
    file.close()

with open("manejo de archivos\\texto2.txt", "a", encoding="utf-8") as file:
    for x in range(10):
        file.write(f"\nvuelta numero: {x}")
    else:
        file.write("\nFin")
    file.close()
file = open("manejo de archivos\\texto2.txt", "r")
# leer una sola linea
print(file.readline())
# leer todas las lineas
# determina desde que posicion empezar a leer el archivo
file.seek(0)
lista1 = file.readlines()
print(lista1)


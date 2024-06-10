import csv
datos = {
    "matias": ["hombre", 25, "arroyo de los patos"],
    "nicolas": ["hombre", 23, "mina clavero"]
}
# with open("manejo de archivos\\Libro1.xlsx", "w") as file:
#     file.write("hola excel")
#     file.close()
with open("manejo de archivos\\Libro1.csv", "w") as file:
    for key, value in datos.items():
        for x in range(len(value)):
            file.write(f"{value[x]} ")
        file.write("\n")
    file.close()
with open("manejo de archivos\\Libro2.csv", "w") as file:
    writer = csv.writer(file)
    for key, value in datos.items():
        for x in range(len(value)):
            writer.writerow(value[x:x+1])
    file.close()

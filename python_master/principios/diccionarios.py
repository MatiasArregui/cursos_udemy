diccionario_1 = {"nombre": "matias", "edad":25, "provincia":"Cordoba"}
print(diccionario_1)
diccionario_1["ocupacion"] = "estudiante"
print(diccionario_1)
del diccionario_1["ocupacion"]
print(diccionario_1)
print()
user = {
    "matias":{"id":1, "carrera":"programador", "edad":25},
    "nahuel":{"id":2, "carrera":"barbero", "edad":23},
    "david":{"id":3, "carrera":"programador", "edad":20}
}
for usuario in user:
    print(f"{usuario}: ",end="")
    for key in user[usuario]:
        print(user[usuario][key], end=" ")
    print()

# for key in diccionario_1:
#     print(key)
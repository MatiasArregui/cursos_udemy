from mysql import connector

mi_db = connector.connect(
    host = "localhost",
    user = "root",
    password = "formis88"
)

cursor = mi_db.cursor()

consulta_1 = "CREATE DATABASE IF NOT EXISTS practicas"
cursor.execute(consulta_1)
consulta_2 = "SHOW DATABASES"
cursor.execute(consulta_2)
print(*cursor)
# lista = [x for x in cursor]
# for x in lista:
#     print(x)
# consulta_3 = "DROP DATABASE practicas"
# cursor.execute(consulta_3)
cursor.execute(consulta_2)
print(*cursor)
mi_db.close()
from mysql import connector

def realizarConsulta(db, consulta):
    cursor = db.cursor()
    cursor.execute(consulta)
    lista = [x for x in cursor]
    return lista


mi_db = connector.connect(
    host = "localhost",
    user = "root",
    password = "formis88",
    database = "practicas"
)
cursor = mi_db.cursor()

#Crear tabla en mysql
consulta = """CREATE TABLE IF NOT EXISTS alumnos(
                nombre VARCHAR(255),
                apellido VARCHAR(255))"""
cursor.execute(consulta)

#Cargar datos a la tabla
consulta = "INSERT INTO alumnos (nombre, apellido) VALUES ('Matias', 'Arregui')"
cursor.execute(consulta)
consulta = "INSERT INTO alumnos (nombre, apellido) VALUES ('Nicolas', 'Arregui')"
cursor.execute(consulta)
#Mostrar datos de la tabla
consulta = "SELECT * FROM alumnos"
# cursor.execute(consulta)
# print(*cursor)
print(*realizarConsulta(mi_db, consulta))

realizarConsulta(mi_db, "DROP TABLE IF EXISTS alumnos")
print(*realizarConsulta(mi_db, "SHOW TABLES"))
#Cerrar database
mi_db.close()
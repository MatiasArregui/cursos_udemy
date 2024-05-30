from mysql import connector

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

#Mostrar datos de la tabla
consulta = "SELECT * FROM alumnos"
cursor.execute(consulta)
print(*cursor)
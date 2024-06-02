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

consulta = "DROP TABLE IF EXISTS alumnos"
cursor.execute(consulta)

consulta = """ CREATE TABLE IF NOT EXISTS alumnos(
                    id INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50),
                    apellido VARCHAR(50))"""
                    
# int(50) not null auto_increment primary key
cursor.execute(consulta)
consulta = """INSERT INTO alumnos VALUES( 0,'matias', 'garcia')"""
cursor.execute(consulta)

#INSERTAR VALORES POR FUERA DE LA CONSULTA POR MEDIO DE UNA TUPLA
# consulta = """INSERT INTO alumnos(nombre,apellido) VALUES (%s, %s), (%s, %s)"""
consulta = """INSERT INTO alumnos VALUES (0, %s, %s), (0, %s, %s)"""
valores = ('matias', 'arregui', 'Nicolas', 'Arregui')
cursor.execute(consulta, valores)

consulta = "SELECT * FROM alumnos"
print(*realizarConsulta(mi_db, consulta))

consulta2 = """INSERT INTO alumnos(nombre, apellido) VALUES (%s, %s)"""
valores2 = [('paula', 'garcia'), ("abril", "arregui")]
cursor.executemany(operation=consulta2, seq_params=valores2)

# DELETE from [table name] where [field name] = ‘whatever’;
consulta = """DELETE FROM alumnos WHERE id=2"""
print(*realizarConsulta(mi_db, consulta))
consulta = "SELECT * FROM alumnos"
print(*realizarConsulta(mi_db, consulta))

# El commit() permite mandar la informacion a la base de datos permitiendo el registro
mi_db.commit()
mi_db.close()


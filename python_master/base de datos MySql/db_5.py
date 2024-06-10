from mysql import connector

db = connector.connect(
    host = "localhost",
    user = "root",
    password = "formis88",
    database = "vivero"
)
cursor = db.cursor()

sql = """INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)"""
clientes = [("nahuel", "arregui"), ("daniela", "grandini"), ("milagros", "sampo")]
cursor.executemany(sql,clientes)

sql = """SELECT nombre, apellido FROM cliente"""
cursor.execute(sql)
print(*cursor)

sql = """DELETE FROM cliente WHERE nombre=%s"""
valor = ('milagros', )
cursor.execute(sql,valor)

# sql = """DELETE FROM cliente WHERE nombre=%s"""
# valor = [('milagros',), ('daniela',), ("nahuel",)]
# cursor.executemany(sql,valor)

sql = """SELECT nombre, apellido FROM cliente"""
cursor.execute(sql)
print(*cursor)

sql = """UPDATE cliente SET nombre='dario' WHERE nombre=%s"""
valor = ("nahuel",)
cursor.execute(sql, valor)

sql = """SELECT nombre, apellido FROM cliente"""
cursor.execute(sql)
print(*cursor)

db.commit()
db.close()
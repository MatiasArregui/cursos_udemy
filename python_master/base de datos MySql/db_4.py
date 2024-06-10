from mysql import connector

db = connector.connect(
    host = "localhost",
    user = "root",
    password = "formis88",
    database = "vivero"
)

cursor = db.cursor()
sql = """CREATE DATABASE IF NOT EXISTS vivero"""
cursor.execute(sql)

sql = """CREATE TABLE IF NOT EXISTS cliente(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50))"""
cursor.execute(sql)

sql = """INSERT INTO cliente(nombre, apellido) VALUES (%s, %s)"""
valores = [("paula", "garcia"), ("mauricio","arregui")]
cursor.executemany(sql, valores)

sql = """DELETE FROM cliente WHERE id > 2"""
cursor.execute(sql)


sql = """SELECT nombre FROM cliente"""
cursor.execute(sql)
print(*cursor)

# sql = """DROP TABLE cliente"""
# cursor.execute(sql)
# print(*cursor)

# sql = """DESCRIBE cliente"""
# cursor.execute(sql)
# print(*cursor)





db.commit()
db.close()
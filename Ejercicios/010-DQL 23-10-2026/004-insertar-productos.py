import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
cursor.execute("DROP TABLE IF EXISTS productos;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(10050) NOT NULL,
precio DECIMAL(6,2)
);
""")

sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s);"

datos = [
    ("Teclado", 25.00),
    ("Raton", 12.50),
    ("Monitor", 140.00),
    ("Altavoces", 30.00)
]

cursor.executemany(sql,datos)

conexion.commit()
print(cursor.rowcount, "filas insertadas")

cursor.close()
conexion.close()

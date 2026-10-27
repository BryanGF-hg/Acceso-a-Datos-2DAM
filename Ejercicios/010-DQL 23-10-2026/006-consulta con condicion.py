import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
print("--Productos de menos de 30 euros---")
sql = "SELECT nombre, precio FROM productos WHERE precio < %s"
cursor.execute(sql, (30,))

for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]}")

conexion.commit()
cursor.close()
conexion.close()

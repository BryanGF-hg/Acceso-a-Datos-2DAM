import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
print("---Todos los productos---")
cursor.execute("SELECT*FROM productos;")
for filas in cursor.fetchall():
 print(filas)


conexion.commit()
cursor.close()
conexion.close()

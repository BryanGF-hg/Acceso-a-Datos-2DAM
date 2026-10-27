import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
print("Conexión correcta con MySQL")
conexion.commit()
cursor.close()
conexion.close()

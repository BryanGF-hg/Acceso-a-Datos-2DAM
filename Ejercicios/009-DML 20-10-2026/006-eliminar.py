import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="lector",
    password="lector123",
    database="biblioteca"
)

cursor = conexion.cursor()
cursor.execute("DELETE FROM clientes WHERE id = 1;")
conexion.commit()

print("Registro eliminado correctamente.")
cursor.close()
conexion.close()

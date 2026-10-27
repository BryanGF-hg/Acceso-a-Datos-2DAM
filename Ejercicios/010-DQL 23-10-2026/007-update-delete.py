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
sql = "UPDATE productos SET precio = %s where nombre = %s;"
cursor.execute(sql, (120, "Monitor"))
print("Filas modificadas:", cursor.rowcount)

sql = "DELETE FROM productos WHERE nombre = %s;"
cursor.execute(sql, ("Raton",))
print("Filas borradas:", cursor.rowcount)


conexion.commit()

print("--- Productos después de los cambios ---")
cursor.execute("SELECT * FROM productos;")
for fila in cursor.fetchall():
    print(f"{fila[0]} | {fila[1]} | {fila[2]}")
    
cursor.close()
conexion.close()

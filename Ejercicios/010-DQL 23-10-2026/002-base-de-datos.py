import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tienda (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
descripcion VARCHAR(50)
);
""")
cursor.execute("SHOW DATABASES;")
print("Base de datos:")
for tabla in cursor.fetchall():
    print("-", tabla[0])
    
cursor.execute('SELECT DATABASE()')
fila = cursor.fetchone()
print("Base de datos seleccionada:", fila[0])

conexion.commit()
cursor.close()
conexion.close()

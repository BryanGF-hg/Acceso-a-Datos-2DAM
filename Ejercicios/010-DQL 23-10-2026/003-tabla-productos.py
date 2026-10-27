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
cursor.execute("SHOW TABLES;")
print("Tabla:")
for tabla in cursor.fetchall():
    print("-", tabla[0])

conexion.commit()
cursor.close()
conexion.close()

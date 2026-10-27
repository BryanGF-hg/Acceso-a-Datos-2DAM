import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="lector",
    password="lector123",
    database="biblioteca"
)
cursor = conexion.cursor()
cursor.execute("DROP TABLE IF EXISTS clientes;")
cursor.execute("""
    CREATE TABLE clientes (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(50),
        apellido VARCHAR(100),
        correo VARCHAR(200)
    );
""")
cursor.execute("""
    INSERT INTO clientes VALUES(
      NULL,
      "Ana",
      "Martinez Ruiz",
      "ana@martinezruiz.com"
    );
""")
conexion.commit()
cursor.close()
conexion.close()

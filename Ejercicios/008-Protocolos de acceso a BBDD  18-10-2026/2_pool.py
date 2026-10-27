from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mivariablepool",
    pool_size=6,
    host="localhost",
    user="lector",
    password="lector123",
    database="biblioteca"
)

for i in range(6):
    conexion = pool.get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT CONNECTION_ID()")
    print("Petición", i + 1, "-> sesión", cursor.fetchone()[0])
    cursor.close()
    conexion.close()

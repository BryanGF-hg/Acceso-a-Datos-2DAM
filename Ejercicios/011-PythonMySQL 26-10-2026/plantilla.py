import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca"
)
cursor = conexion.cursor()
cursor.execute("""
SQL
""")

conexion.commit()
cursor.close()
conexion.close()

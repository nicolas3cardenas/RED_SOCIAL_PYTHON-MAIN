import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="red_social"
            )
            if self.con.is_connected():
                print("✅ Conexión exitosa con la base de datos.")
        except Error as e:
            print(f"❌ Error de conexión: {e}")
            self.con = None

    def obtener_conexion(self):
        return self.con

    def cerrar(self):
        if self.con and self.con.is_connected():
            self.con.close()
            print("🔒 Conexión cerrada correctamente.")

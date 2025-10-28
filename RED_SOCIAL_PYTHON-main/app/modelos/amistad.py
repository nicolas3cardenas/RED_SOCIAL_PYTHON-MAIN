# app/modelos/amistad.py
from app.config.conexion import Conexion

class Amistad:
    def __init__(self, usuario_id_1, usuario_id_2):
        self.usuario_id_1 = usuario_id_1
        self.usuario_id_2 = usuario_id_2

    def guardar(self):
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: no hay conexión a la base de datos.")
            return False
        try:
            # Guardamos con el orden tal cual; la tabla puede tener UNIQUE sobre (LEAST, GREATEST) para evitar duplicados
            cur = con.cursor()
            sql = "INSERT INTO amistad (usuario_id_1, usuario_id_2) VALUES (%s, %s)"
            cur.execute(sql, (self.usuario_id_1, self.usuario_id_2))
            con.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Error al guardar amistad: {e}")
            return False

    @staticmethod
    def listar_amigos(usuario_id):
        con = Conexion().obtener_conexion()
        if not con:
            return []
        cur = con.cursor(dictionary=True)
        cur.execute("""
            SELECT u.id, u.nombre, u.correo
            FROM usuario u
            JOIN amistad a ON
              (a.usuario_id_1 = %s AND u.id = a.usuario_id_2)
              OR (a.usuario_id_2 = %s AND u.id = a.usuario_id_1)
        """, (usuario_id, usuario_id))
        filas = cur.fetchall()
        cur.close()
        return filas

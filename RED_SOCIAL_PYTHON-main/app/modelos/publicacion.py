# app/modelos/publicacion.py
from app.config.conexion import Conexion

class Publicacion:
    def __init__(self, usuario_id, contenido):
        self.usuario_id = usuario_id
        self.contenido = contenido
        self.id = None

    def guardar(self):
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: no hay conexión a la base de datos.")
            return False
        try:
            cur = con.cursor()
            sql = "INSERT INTO publicacion (usuario_id, contenido) VALUES (%s, %s)"
            cur.execute(sql, (self.usuario_id, self.contenido))
            con.commit()
            self.id = cur.lastrowid
            cur.close()
            return self.id
        except Exception as e:
            print(f"Error al guardar publicación: {e}")
            return False

    @staticmethod
    def listar_todas():
        con = Conexion().obtener_conexion()
        if not con:
            return []
        cur = con.cursor(dictionary=True)
        cur.execute("""
            SELECT p.id, p.usuario_id, p.contenido, p.fecha, u.nombre
            FROM publicacion p
            JOIN usuario u ON p.usuario_id = u.id
            ORDER BY p.fecha DESC
        """)
        filas = cur.fetchall()
        cur.close()
        return filas

# app/modelos/like.py
from app.config.conexion import Conexion

class Like:
    def __init__(self, usuario_id, publicacion_id):
        self.usuario_id = usuario_id
        self.publicacion_id = publicacion_id

    def guardar(self):
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: no hay conexión a la base de datos.")
            return False
        try:
            cur = con.cursor()
            sql = "INSERT INTO likes (usuario_id, publicacion_id) VALUES (%s, %s)"
            cur.execute(sql, (self.usuario_id, self.publicacion_id))
            con.commit()
            cur.close()
            return True
        except Exception as e:
            # puede fallar por duplicado si hay constraint
            print(f"Error al guardar like: {e}")
            return False

    @staticmethod
    def contar_por_publicacion(publicacion_id):
        con = Conexion().obtener_conexion()
        if not con:
            return 0
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM likes WHERE publicacion_id = %s", (publicacion_id,))
        row = cur.fetchone()
        cur.close()
        return row[0] if row else 0

    @staticmethod
    def usuarios_que_dieron_like(publicacion_id):
        con = Conexion().obtener_conexion()
        if not con:
            return []
        cur = con.cursor(dictionary=True)
        cur.execute("""
            SELECT u.id, u.nombre, u.correo
            FROM usuario u
            JOIN likes l ON u.id = l.usuario_id
            WHERE l.publicacion_id = %s
        """, (publicacion_id,))
        filas = cur.fetchall()
        cur.close()
        return filas

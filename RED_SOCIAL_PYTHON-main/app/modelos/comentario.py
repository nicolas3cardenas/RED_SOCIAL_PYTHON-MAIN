from app.config.conexion import Conexion
from mysql.connector import Error

class Comentario:
    def __init__(self, publicacion_id, usuario_id, contenido):
        self.publicacion_id = publicacion_id
        self.usuario_id = usuario_id
        self.contenido = contenido

    def guardar(self):
        """Guarda el comentario en la base de datos"""
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: no se pudo establecer conexión con la base de datos.")
            return False
        try:
            cursor = con.cursor()
            sql = """
                INSERT INTO comentario (publicacion_id, usuario_id, contenido)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (self.publicacion_id, self.usuario_id, self.contenido))
            con.commit()
            print(f"Comentario guardado correctamente (usuario {self.usuario_id} -> publicación {self.publicacion_id})")
            return True
        except Error as e:
            print(f"Error al guardar comentario: {e}")
            return False
        finally:
            if con.is_connected():
                con.close()

    @staticmethod
    def listar_por_publicacion(publicacion_id):
        """Lista los comentarios asociados a una publicación"""
        con = Conexion().obtener_conexion()
        if not con:
            return []
        try:
            cursor = con.cursor(dictionary=True)
            sql = """
                SELECT c.id, c.contenido, c.fecha, u.nombre
                FROM comentario c
                JOIN usuario u ON c.usuario_id = u.id
                WHERE c.publicacion_id = %s
                ORDER BY c.fecha DESC
            """
            cursor.execute(sql, (publicacion_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error al listar comentarios: {e}")
            return []
        finally:
            if con.is_connected():
                con.close()

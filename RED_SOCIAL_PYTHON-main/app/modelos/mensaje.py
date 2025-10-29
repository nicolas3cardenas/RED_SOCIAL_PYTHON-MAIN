from app.config.conexion import Conexion

class Mensaje:
    def __init__(self, remitente_id, destinatario_id, contenido):
        self.remitente_id = remitente_id
        self.destinatario_id = destinatario_id
        self.contenido = contenido

    def guardar(self):
        """Guarda un nuevo mensaje en la base de datos."""
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: No hay conexión con la base de datos.")
            return False
        try:
            cursor = con.cursor()
            sql = """
                INSERT INTO mensaje (remitente_id, destinatario_id, contenido)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (self.remitente_id, self.destinatario_id, self.contenido))
            con.commit()
            print(f"Mensaje enviado de {self.remitente_id} a {self.destinatario_id}.")
            return True
        except Exception as e:
            print(f"Error al guardar el mensaje: {e}")
            return False
        finally:
            con.close()

    @staticmethod
    def listar_conversacion(usuario1_id, usuario2_id):
        """Muestra los mensajes entre dos usuarios (en ambos sentidos)."""
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: No hay conexión con la base de datos.")
            return []
        try:
            cursor = con.cursor(dictionary=True)
            sql = """
                SELECT 
                    m.id,
                    m.remitente_id,
                    r.nombre AS remitente,
                    m.destinatario_id,
                    d.nombre AS destinatario,
                    m.contenido,
                    m.fecha
                FROM mensaje m
                JOIN usuario r ON m.remitente_id = r.id
                JOIN usuario d ON m.destinatario_id = d.id
                WHERE 
                    (m.remitente_id = %s AND m.destinatario_id = %s)
                    OR
                    (m.remitente_id = %s AND m.destinatario_id = %s)
                ORDER BY m.fecha ASC
            """
            cursor.execute(sql, (usuario1_id, usuario2_id, usuario2_id, usuario1_id))
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al listar la conversación: {e}")
            return []
        finally:
            con.close()

# app/modelos/usuario.py
from app.config.conexion import Conexion

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def guardar(self):
        con = Conexion().obtener_conexion()
        if not con:
            print("Error: no hay conexión a la base de datos.")
            return False
        try:
            cur = con.cursor()
            sql = "INSERT INTO usuario (nombre, correo) VALUES (%s, %s)"
            cur.execute(sql, (self.nombre, self.correo))
            con.commit()
            last_id = cur.lastrowid
            cur.close()
            return last_id
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
            return False

    @staticmethod
    def listar_todos():
        con = Conexion().obtener_conexion()
        if not con:
            return []
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT id, nombre, correo, creado_at FROM usuario ORDER BY id ASC")
        filas = cur.fetchall()
        cur.close()
        return filas

    @staticmethod
    def obtener_por_id(usuario_id):
        con = Conexion().obtener_conexion()
        if not con:
            return None
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT id, nombre, correo, creado_at FROM usuario WHERE id = %s", (usuario_id,))
        fila = cur.fetchone()
        cur.close()
        return fila

# tests/test_conexion.py
from app.config.conexion import Conexion

def main():
    print("Prueba de conexión:")
    c = Conexion()
    con = c.obtener_conexion()
    if con:
        print("Conexión OK")
        c.cerrar()
    else:
        print("Conexión FALLIDA")

if __name__ == "__main__":
    main()

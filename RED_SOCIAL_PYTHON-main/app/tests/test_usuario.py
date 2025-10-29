# tests/test_usuario.py
from app.modelos.usuario import Usuario

def main():
    print("=== TEST USUARIO ===")
    u = Usuario("Ana Prueba", "ana.prueba@example.com")
    res = u.guardar()
    print("Guardar retornó:", res)
    usuarios = Usuario.listar_todos()
    print("Usuarios (muestra):")
    for x in usuarios[:5]:
        print(x)

if __name__ == "__main__":
    main()

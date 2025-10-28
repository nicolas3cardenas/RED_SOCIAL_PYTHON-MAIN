# tests/test_publicacion.py
from app.modelos.publicacion import Publicacion
from app.modelos.usuario import Usuario

def main():
    print("=== TEST PUBLICACION ===")
    # Aseguramos que exista al menos un usuario
    usuarios = Usuario.listar_todos()
    if not usuarios:
        u = Usuario("UsuarioTestPub", "testpub@example.com")
        u.guardar()
        usuarios = Usuario.listar_todos()

    usuario_id = usuarios[0]['id']
    p = Publicacion(usuario_id, "Publicación de prueba desde test_publicacion")
    pid = p.guardar()
    print("ID publicación creada:", pid)
    pubs = Publicacion.listar_todas()
    print("Publicaciones (muestra):")
    for r in pubs[:5]:
        print(r)

if __name__ == "__main__":
    main()

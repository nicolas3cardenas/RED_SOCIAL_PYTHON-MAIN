# tests/test_like.py
from app.modelos.like import Like
from app.modelos.publicacion import Publicacion
from app.modelos.usuario import Usuario

def main():
    print("=== TEST LIKE ===")
    usuarios = Usuario.listar_todos()
    if len(usuarios) < 2:
        u1 = Usuario("User1", "u1@example.com"); u1.guardar()
        u2 = Usuario("User2", "u2@example.com"); u2.guardar()
        usuarios = Usuario.listar_todos()

    publicaciones = Publicacion.listar_todas()
    if not publicaciones:
        Publicacion(usuarios[0]['id'], "Public test for likes").guardar()
        publicaciones = Publicacion.listar_todas()

    pub_id = publicaciones[0]['id']
    usuario_like = usuarios[1]['id']
    like = Like(usuario_like, pub_id)
    ok = like.guardar()
    print("Like guardado:", ok)
    print("Total likes en publicación", pub_id, ":", Like.contar_por_publicacion(pub_id))
    print("Usuarios que dieron like:")
    for u in Like.usuarios_que_dieron_like(pub_id):
        print(u)

if __name__ == "__main__":
    main()

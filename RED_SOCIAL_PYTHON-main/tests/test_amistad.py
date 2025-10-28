# tests/test_amistad.py
from app.modelos.amistad import Amistad
from app.modelos.usuario import Usuario

def main():
    print("=== TEST AMISTAD ===")
    usuarios = Usuario.listar_todos()
    if len(usuarios) < 2:
        Usuario("Amigo1", "a1@example.com").guardar()
        Usuario("Amigo2", "a2@example.com").guardar()
        usuarios = Usuario.listar_todos()

    id1 = usuarios[0]['id']
    id2 = usuarios[1]['id']
    a = Amistad(id1, id2)
    ok = a.guardar()
    print("Amistad guardada:", ok)
    amigos_de_1 = Amistad.listar_amigos(id1)
    print("Amigos de", id1, ":", amigos_de_1)

if __name__ == "__main__":
    main()

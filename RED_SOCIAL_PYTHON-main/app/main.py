from app.modelos.usuario import Usuario
from app.modelos.publicacion import Publicacion
from app.modelos.like import Like
from app.modelos.amistad import Amistad
from app.modelos.comentario import Comentario
from app.modelos.mensaje import Mensaje
from prettytable import PrettyTable


def mostrar_menu():
    print("\n===============================")
    print("      MENU RED SOCIAL PYTHON   ")
    print("===============================")
    print("1.  Registrar nuevo usuario")
    print("2.  Ver todos los usuarios")
    print("-------------------------------")
    print("3.  Crear publicación")
    print("4.  Ver todas las publicaciones")
    print("5.  Dar 'Me Gusta' (Like)")
    print("6.  Comentar publicación")
    print("-------------------------------")
    print("7.  Enviar solicitud de amistad")
    print("8.  Ver amigos de un usuario")
    print("-------------------------------")
    print("9.  Enviar mensaje privado")
    print("10. Ver conversación entre usuarios")
    print("-------------------------------")
    print("0.  Salir")
    print("===============================")
    return input("Elige una opción: ")


# --- Funciones de Utilidad ---

def registrar_usuario():
    print("\n--- REGISTRAR NUEVO USUARIO ---")
    nombre = input("Ingresa el nombre: ")
    correo = input("Ingresa el correo: ")
    try:
        u = Usuario(nombre, correo)
        u.guardar()
    except Exception as e:
        print(f"Error al registrar: {e}")


def listar_usuarios():
    print("\n--- LISTADO DE USUARIOS ---")
    usuarios = Usuario.listar_todos()
    if not usuarios:
        print("No hay usuarios registrados.")
        return []
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Correo", "Fecha Registro"]
    for u in usuarios:
        tabla.add_row([u["id"], u["nombre"], u["correo"], u["creado_at"]])
    print(tabla)
    return usuarios


def crear_publicacion():
    usuarios = listar_usuarios()
    if not usuarios:
        return
    try:
        usuario_id = int(input("Ingresa el ID del usuario que publica: "))
        if not any(u['id'] == usuario_id for u in usuarios):
            print("Error: ID de usuario no válido.")
            return
        contenido = input("Escribe el contenido de la publicación: ")
        pub = Publicacion(usuario_id, contenido)
        if pub.guardar():
            print(f"Publicación creada correctamente.")
        else:
            print("No se pudo crear la publicación.")
    except Exception as e:
        print(f"Error: {e}")


def listar_publicaciones():
    print("\n--- LISTADO DE PUBLICACIONES ---")
    publicaciones = Publicacion.listar_todas()
    if not publicaciones:
        print("No hay publicaciones.")
        return []
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Autor", "Contenido", "Likes", "Fecha"]
    for p in publicaciones:
        likes = Like.contar_por_publicacion(p["id"])
        tabla.add_row([p["id"], p["nombre"], p["contenido"][:40] + "...", likes, p["fecha"].strftime("%Y-%m-%d %H:%M")])
    print(tabla)
    return publicaciones


def dar_like():
    publicaciones = listar_publicaciones()
    if not publicaciones:
        return
    listar_usuarios()
    try:
        usuario_id = int(input("Ingresa tu ID de usuario: "))
        publicacion_id = int(input("Ingresa el ID de la publicación: "))
        l = Like(usuario_id, publicacion_id)
        l.guardar()
    except Exception as e:
        print(f"Error: {e}")


def comentar_publicacion():
    publicaciones = listar_publicaciones()
    if not publicaciones:
        return
    listar_usuarios()
    try:
        publicacion_id = int(input("ID de la publicación a comentar: "))
        usuario_id = int(input("Tu ID de usuario: "))
        contenido = input("Escribe tu comentario: ")
        c = Comentario(publicacion_id, usuario_id, contenido)
        c.guardar()
    except Exception as e:
        print(f"Error al comentar: {e}")


def enviar_amistad():
    usuarios = listar_usuarios()
    if not usuarios:
        return
    try:
        id1 = int(input("Ingresa tu ID: "))
        id2 = int(input("Ingresa el ID del amigo: "))
        if id1 == id2:
            print("No puedes enviarte amistad a ti mismo.")
            return
        a = Amistad(id1, id2)
        a.guardar()
    except Exception as e:
        print(f"Error: {e}")


def ver_amigos():
    listar_usuarios()
    try:
        usuario_id = int(input("Ingresa el ID del usuario para ver sus amigos: "))
        amigos = Amistad.listar_amigos(usuario_id)
        if not amigos:
            print("Este usuario no tiene amigos.")
            return
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Correo"]
        for a in amigos:
            tabla.add_row([a["id"], a["nombre"], a["correo"]])
        print(tabla)
    except Exception as e:
        print(f"Error: {e}")


def enviar_mensaje():
    usuarios = listar_usuarios()
    if not usuarios:
        return
    try:
        remitente_id = int(input("Tu ID (remitente): "))
        destinatario_id = int(input("ID del destinatario: "))
        contenido = input("Contenido del mensaje: ")
        m = Mensaje(remitente_id, destinatario_id, contenido)
        m.guardar()
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")


def ver_conversacion():
    try:
        id1 = int(input("ID del primer usuario: "))
        id2 = int(input("ID del segundo usuario: "))
        mensajes = Mensaje.listar_conversacion(id1, id2)
        if not mensajes:
            print("No hay mensajes entre estos usuarios.")
            return
        print(f"\n--- CONVERSACIÓN ENTRE {id1} Y {id2} ---")
        for m in mensajes:
            print(f"[{m['fecha']}] {m['remitente']} -> {m['destinatario']}: {m['contenido']}")
    except Exception as e:
        print(f"Error: {e}")


# --- Bucle Principal ---

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            listar_usuarios()
        elif opcion == '3':
            crear_publicacion()
        elif opcion == '4':
            listar_publicaciones()
        elif opcion == '5':
            dar_like()
        elif opcion == '6':
            comentar_publicacion()
        elif opcion == '7':
            enviar_amistad()
        elif opcion == '8':
            ver_amigos()
        elif opcion == '9':
            enviar_mensaje()
        elif opcion == '10':
            ver_conversacion()
        elif opcion == '0':
            print("Saliendo de la aplicación. Hasta pronto.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()

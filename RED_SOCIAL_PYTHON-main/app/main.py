from app.modelos.usuario import Usuario
from app.modelos.publicacion import Publicacion
from app.modelos.like import Like
from app.modelos.amistad import Amistad
from prettytable import PrettyTable


def mostrar_menu():
    print("\n===============================")
    print("      MENU RED SOCIAL PYTHON   ")
    print("===============================")
    print("1.  Registrar nuevo usuario")
    print("2.  Ver todos los usuarios")
    print("-------------------------------")
    print("3.  Crear publicacion")
    print("4.  Ver todas las publicaciones")
    print("5.  Dar 'Me Gusta' (Like)")
    print("-------------------------------")
    print("6.  Enviar solicitud de amistad")
    print("7.  Ver amigos de un usuario")
    print("-------------------------------")
    print("0.  Salir")
    print("===============================")
    return input("Elige una opcion: ")

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

    # --- Mostrar usuarios con PrettyTable ---
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
            print("Error: ID de usuario no valido.")
            return
        
        contenido = input("Escribe el contenido de la publicacion: ")
        
        pub = Publicacion(usuario_id, contenido)
        if pub.guardar():
            print(f"Publicacion creada con ID: {pub.id}")
        else:
            print("No se pudo crear la publicacion.")
    except ValueError:
        print("Error: Debes ingresar un numero valido para el ID.")
    except Exception as e:
        print(f"Error: {e}")

def listar_publicaciones():
    print("\n--- LISTADO DE PUBLICACIONES ---")
    publicaciones = Publicacion.listar_todas()
    if not publicaciones:
        print("No hay publicaciones.")
        return []
    for p in publicaciones:
        print(f"ID: {p['id']} | Autor: {p['nombre']} (ID: {p['usuario_id']})")
        print(f"Contenido: {p['contenido'][:50]}...")
        likes = Like.contar_por_publicacion(p['id'])
        print(f"[{p['fecha'].strftime('%Y-%m-%d %H:%M')}] | Me gusta: {likes}")
        print("-" * 30)
    return publicaciones

def dar_like():
    publicaciones = listar_publicaciones()
    if not publicaciones:
        return
    
    listar_usuarios()
    
    try:
        usuario_id = int(input("Ingresa tu ID de usuario (quien da like): "))
        publicacion_id = int(input("Ingresa el ID de la publicacion a la que daras like: "))
        
        l = Like(usuario_id, publicacion_id)
        l.guardar()
    except ValueError:
        print("Error: Debes ingresar IDs numericos validos.")
    except Exception as e:
        print(f"Error: {e}")

def enviar_amistad():
    usuarios = listar_usuarios()
    if not usuarios:
        return

    try:
        id1 = int(input("Ingresa tu ID de usuario: "))
        id2 = int(input("Ingresa el ID del amigo que quieres agregar: "))
        
        if id1 == id2:
            print("No puedes enviarte amistad a ti mismo.")
            return

        a = Amistad(id1, id2)
        if a.guardar():
            print(f"Solicitud enviada (Amistad registrada entre {id1} y {id2}).")
        else:
            print("No se pudo registrar la amistad. (Podria ser que ya son amigos o los IDs son invalidos).")

    except ValueError:
        print("Error: Debes ingresar IDs numericos validos.")
    except Exception as e:
        print(f"Error: {e}")

def ver_amigos():
    listar_usuarios()
    try:
        usuario_id = int(input("Ingresa el ID del usuario para ver sus amigos: "))
        amigos = Amistad.listar_amigos(usuario_id)
        
        print(f"\n--- AMIGOS DEL USUARIO ID: {usuario_id} ---")
        if not amigos:
            print("Este usuario no tiene amigos registrados.")
            return
        
        # --- Mostrar amigos con PrettyTable ---
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Correo"]
        for a in amigos:
            tabla.add_row([a["id"], a["nombre"], a["correo"]])
        print(tabla)
            
    except ValueError:
        print("Error: Debes ingresar un ID numerico valido.")
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
            enviar_amistad()
        elif opcion == '7':
            ver_amigos()
        elif opcion == '0':
            print("Saliendo de la aplicacion. Hasta pronto.")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()

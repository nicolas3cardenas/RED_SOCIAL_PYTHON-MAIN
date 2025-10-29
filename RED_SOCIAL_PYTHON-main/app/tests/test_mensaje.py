from app.modelos.mensaje import Mensaje

def test_mensaje():
    print("=== TEST MENSAJE PRIVADO ===")

    # Enviar un mensaje de un usuario a otro
    m = Mensaje(remitente_id=1, destinatario_id=2, contenido="Hola, ¿cómo estás?")
    resultado = m.guardar()
    print("Mensaje guardado:", resultado)

    # Listar la conversación entre los dos usuarios
    conversacion = Mensaje.listar_conversacion(1, 2)
    print("Conversación (1 <-> 2):")
    for msg in conversacion:
        print(f"[{msg['fecha']}] {msg['remitente']} → {msg['destinatario']}: {msg['contenido']}")

if __name__ == "__main__":
    test_mensaje()

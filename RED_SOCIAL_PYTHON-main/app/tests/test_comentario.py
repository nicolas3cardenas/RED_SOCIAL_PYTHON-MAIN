from app.modelos.comentario import Comentario

print("=== TEST COMENTARIO ===")

# Crear un comentario de prueba
comentario = Comentario(publicacion_id=2, usuario_id=1, contenido="Excelente publicación de prueba")
resultado = comentario.guardar()
print("Guardar retornó:", resultado)

# Listar comentarios de una publicación
comentarios = Comentario.listar_por_publicacion(2)
print("Comentarios en la publicación 2:")
for c in comentarios:
    print(c)

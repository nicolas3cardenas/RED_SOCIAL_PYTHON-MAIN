# COMANDOS ÚTILES – RED_SOCIAL_PYTHON

## 1. Entorno virtual

Crear entorno virtual:
```bash
python -m venv venv
```

Activar entorno (Windows):
```bash
venv\Scripts\activate
```

Desactivar entorno:
```bash
deactivate
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Verificar instalación:
```bash
pip list
```

Debe mostrar algo como:
```
mysql-connector-python  9.4.0
prettytable             3.16.0
```

---

## 2. Estructura general del proyecto

```
RED_SOCIAL_PYTHON-main/
│
├── app/
│   ├── auxiliares/
│   │   ├── info_app.py
│   │   └── version.py
│   │
│   ├── config/
│   │   ├── conexion.py
│   │   ├── guardar_datos.py
│   │   └── obtener_datos.py
│   │
│   ├── iu/
│   │   └── menus.py
│   │
│   ├── modelos/
│   │   ├── usuario.py
│   │   ├── publicacion.py
│   │   ├── like.py
│   │   └── amistad.py
│   │
│   ├── datos/
│   │   └── sql/
│   │       ├── ddl_red_social.sql
│   │       └── dml_red_social.sql
│   │
│   └── main.py
│
├── tests/
│   ├── test_conexion.py
│   ├── test_usuario.py
│   ├── test_publicacion.py
│   ├── test_like.py
│   └── test_amistad.py
│
├── COMANDOS.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 3. Ejecución de pruebas

Cada módulo de prueba se ejecuta desde la raíz del proyecto:
```bash
python -m tests.test_conexion
python -m tests.test_usuario
python -m tests.test_publicacion
python -m tests.test_like
python -m tests.test_amistad
```

Ejecutar todas las pruebas (opcional):
```bash
pytest tests/
```

---

## 4. Base de datos MySQL

Ejecutar el script de creación (DDL):
```bash
mysql -u root -p red_social < app/datos/sql/ddl_red_social.sql
```

Insertar datos iniciales (DML):
```bash
mysql -u root -p red_social < app/datos/sql/dml_red_social.sql
```

---

## 5. Ejecución principal del sistema

Iniciar la aplicación:
```bash
python app/main.py
```

Ver información del sistema:
```bash
python -m app.auxiliares.info_app
```

Ver versión:
```bash
python -m app.auxiliares.version
```

---

## 6. Ejemplo rápido en consola

```python
from app.modelos.usuario import Usuario
from app.modelos.publicacion import Publicacion

# Listar usuarios
print(Usuario.listar_todos())

# Crear una publicación
p = Publicacion(usuario_id=1, contenido="Mi primera publicación desde Python")
p.guardar()
```

---

## 7. Notas finales

- Todos los módulos usan la clase `Conexion` definida en `app/config/conexion.py`.  
- Los scripts SQL (`ddl_red_social.sql` y `dml_red_social.sql`) permiten crear y poblar la base de datos.  
- Los tests pueden ejecutarse varias veces sin errores por duplicados.  
- Proyecto probado en Python 3.11 y MySQL Connector 9.4.0.  
- Se recomienda mantener el entorno virtual limpio antes de ejecutar pruebas nuevas.

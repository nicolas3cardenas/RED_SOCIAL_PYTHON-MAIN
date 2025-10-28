```markdown
# Proyecto: Red Social en Python (MySQL + POO)

Este proyecto implementa una mini red social desarrollada en **Python**, aplicando **Programación Orientada a Objetos (POO)** y utilizando **MySQL** como base de datos relacional.

El sistema permite:
- Crear y listar usuarios.  
- Registrar publicaciones.  
- Dar "likes" a publicaciones.  
- Administrar amistades.  

Todo el código está modularizado y probado mediante scripts en el directorio `tests`.

---

## Estructura del proyecto

```

RED_SOCIAL_PYTHON-MAIN/
│
├── app/
│   ├── auxiliares/
│   │   ├── info_app.py
│   │   └── version.py
│   │
│   ├── config/
│   │   ├── **init**.py
│   │   ├── conexion.py
│   │   ├── guardar_datos.py
│   │   └── obtener_datos.py
│   │
│   ├── iu/
│   │   ├── **init**.py
│   │   └── menus.py
│   │
│   ├── modelos/
│   │   ├── **init**.py
│   │   ├── amistad.py
│   │   ├── like.py
│   │   ├── publicacion.py
│   │   └── usuario.py
│   │
│   ├── main.py
│   │
│   └── datos/
│       └── sql/
│           ├── **init**.py
│           ├── ddl_red_social.sql
│           └── dml_red_social.sql
│
├── tests/
│   ├── test_conexion.py
│   ├── test_usuario.py
│   ├── test_publicacion.py
│   ├── test_like.py
│   └── test_amistad.py
│
├── venv/
│
├── .gitignore
├── README.md
├── COMANDOS.md
└── requirements.txt

````

---

## Requisitos previos

- Python **3.11 o superior**  
- **MySQL Server** activo  
- Base de datos llamada **`red_social`**

Archivos SQL incluidos:
- `ddl_red_social.sql`: crea la estructura de las tablas  
- `dml_red_social.sql`: carga datos iniciales de ejemplo

---

## Instalación

1. Crear el entorno virtual:
   ```bash
   python -m venv venv
````

2. Activar entorno:

   ```bash
   venv\Scripts\activate
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Verificar instalación:

   ```bash
   pip list
   ```

   Debe mostrar:

   ```
   mysql-connector-python  9.4.0
   prettytable             3.16.0
   ```

---

## Estructura SQL de la base de datos

```sql
CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(150),
  creado_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publicacion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT,
  contenido TEXT,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE likes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT,
  publicacion_id INT,
  UNIQUE(usuario_id, publicacion_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario(id),
  FOREIGN KEY (publicacion_id) REFERENCES publicacion(id)
);

CREATE TABLE amistad (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id_1 INT,
  usuario_id_2 INT,
  UNIQUE KEY unique_amistad (usuario_id_1, usuario_id_2),
  FOREIGN KEY (usuario_id_1) REFERENCES usuario(id),
  FOREIGN KEY (usuario_id_2) REFERENCES usuario(id)
);
```

---

## Ejecución de pruebas

Desde la raíz del proyecto, ejecutar:

```bash
python -m tests.test_conexion
python -m tests.test_usuario
python -m tests.test_publicacion
python -m tests.test_like
python -m tests.test_amistad
```

---

## Descripción de módulos principales

| Módulo                       | Descripción                                     |
| ---------------------------- | ----------------------------------------------- |
| `conexion.py`                | Maneja la conexión con MySQL                    |
| `usuario.py`                 | Define la clase Usuario y operaciones básicas   |
| `publicacion.py`             | Define publicaciones y su relación con usuarios |
| `like.py`                    | Administra los “me gusta”                       |
| `amistad.py`                 | Gestiona las relaciones de amistad              |
| `menus.py`                   | Interfaz de usuario por consola                 |
| `info_app.py` y `version.py` | Contienen información de la aplicación          |
| `ddl_red_social.sql`         | Script de creación de tablas                    |
| `dml_red_social.sql`         | Script de inserción de datos de ejemplo         |

---

## Ejemplo rápido de uso

```python
from app.modelos.usuario import Usuario

usuarios = Usuario.listar_todos()
for u in usuarios:
    print(u)
```

---

## Autor

**Nicolás cardenas**
Proyecto académico – Programación Orientada a Objetos (Python + MySQL)
Año 2025

```

---


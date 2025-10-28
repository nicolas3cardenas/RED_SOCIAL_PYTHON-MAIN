CREATE DATABASE IF NOT EXISTS red_social;
USE red_social;

CREATE TABLE usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(150) NOT NULL UNIQUE,
  creado_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publicacion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  contenido TEXT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE likes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  publicacion_id INT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY unique_like (usuario_id, publicacion_id),
  FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE,
  FOREIGN KEY (publicacion_id) REFERENCES publicacion(id) ON DELETE CASCADE
);

CREATE TABLE amistad (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id_1 INT NOT NULL,
  usuario_id_2 INT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY unique_amistad (usuario_id_1, usuario_id_2),
  FOREIGN KEY (usuario_id_1) REFERENCES usuario(id) ON DELETE CASCADE,
  FOREIGN KEY (usuario_id_2) REFERENCES usuario(id) ON DELETE CASCADE
);

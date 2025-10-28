USE red_social;

INSERT INTO usuario (nombre, correo) VALUES
('Ana Pérez', 'ana@example.com'),
('Juan Gómez', 'juan@example.com'),
('María Torres', 'maria@example.com'),
('Luis Vega', 'luis@example.com');

INSERT INTO publicacion (usuario_id, contenido) VALUES
(1, 'Bienvenidos a mi primera publicación.'),
(2, 'Qué buen día para aprender Python.'),
(3, 'Estoy probando la red social en desarrollo.');

INSERT INTO likes (usuario_id, publicacion_id) VALUES
(2, 1),
(3, 1),
(1, 2);

INSERT INTO amistad (usuario_id_1, usuario_id_2) VALUES
(1, 2),
(1, 3),
(2, 3);

CREATE DATABASE biblioteca;
USE biblioteca;
 
CREATE TABLE libros (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    titulo     VARCHAR(100),
    autor      VARCHAR(100),
    ejemplares INT
);
 
INSERT INTO libros (titulo, autor, ejemplares) VALUES
    ('Don Quijote de la Mancha', 'Miguel de Cervantes',   3),
    ('Novelas ejemplares',       'Miguel de Cervantes',   1),
    ('La casa de Bernarda Alba', 'Federico García Lorca', 2),
    ('Romancero gitano',         'Federico García Lorca', 0);
 
SELECT * FROM libros;

CREATE USER IF NOT EXISTS 'app_biblioteca'@'localhost' IDENTIFIED BY 'Biblio_2026';
GRANT ALL PRIVILEGES ON biblioteca.* TO 'app_biblioteca'@'localhost';
USE biblioteca;

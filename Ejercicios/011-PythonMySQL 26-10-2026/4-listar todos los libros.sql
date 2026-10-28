USE biblioteca;

DELIMITER //

CREATE PROCEDURE listar_libros()
BEGIN
    SELECT id, titulo, autor, ejemplares
    FROM libros
    ORDER BY id;
END //

DELIMITER ;

USE biblioteca;

DELIMITER //

CREATE PROCEDURE buscar_por_autor(IN p_autor VARCHAR(100))
BEGIN
    SELECT titulo, ejemplares
    FROM libros
    WHERE autor = p_autor
    ORDER BY id;
END //

DELIMITER ;

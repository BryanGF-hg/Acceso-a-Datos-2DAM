USE biblioteca;

DELIMITER //

CREATE PROCEDURE contar_libros(OUT p_total INT)
BEGIN
    SELECT COUNT(*) INTO p_total
    FROM libros;
END //

DELIMITER ;

USE biblioteca;

DELIMITER //

CREATE PROCEDURE prestar_libro(IN p_id INT)
BEGIN
    IF (SELECT ejemplares FROM libros WHERE id = p_id) = 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No quedan ejemplares';
    ELSE
        UPDATE libros
        SET ejemplares = ejemplares - 1
        WHERE id = p_id;
    END IF;
END //

DELIMITER ;

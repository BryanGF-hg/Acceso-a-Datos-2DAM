GRANT EXECUTE ON PROCEDURE biblioteca.listar_libros
TO 'app_biblioteca'@'localhost';

GRANT EXECUTE ON PROCEDURE biblioteca.buscar_por_autor
TO 'app_biblioteca'@'localhost';

GRANT EXECUTE ON PROCEDURE biblioteca.contar_libros
TO 'app_biblioteca'@'localhost';

GRANT EXECUTE ON PROCEDURE biblioteca.prestar_libro
TO 'app_biblioteca'@'localhost';

REVOKE SELECT ON biblioteca.libros
FROM 'app_biblioteca'@'localhost';

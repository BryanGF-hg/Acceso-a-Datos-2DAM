CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'root1234';
GRANT ALL PRIVILEGES ON taquilla.* TO 'root'@'localhost';
DROP DATABASE IF EXISTS taquilla;
CREATE DATABASE taquilla;
USE taquilla;
 
CREATE TABLE clientes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50),
  saldo INT
) ENGINE = InnoDB;
 
CREATE TABLE entradas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cliente_id INT,
  evento VARCHAR(50)
) ENGINE = InnoDB;
/*InnoDb es el tipo de tabla que permite transacciones*/
 
INSERT INTO clientes (nombre, saldo) VALUES ('Laura', 50), ('Marcos', 15);



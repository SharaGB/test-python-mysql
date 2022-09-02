/*
 Teniendo en cuenta los archivos:
 - softpymes_test.png
 - softpymes_test.sql
 Generar scripts que realicen las siguientes consultas:
 */

/* 1. Consultar los items que pertenezcan a la compañia con ID #3 (debe utilizar INNER JOIN) */

SELECT
    c.name AS 'Compañia',
    i.name AS 'Item'
FROM companies c
    INNER JOIN items i ON c.id = i.companyId
WHERE i.companyId = 3;

/* 2. Mostrar los últimos 10 items */

SELECT id, name FROM items ORDER BY id DESC LIMIT 10;

/* 3. Mostrar los items que en el nombre terminen con la letra A */

SELECT
    name as 'Items que terminan con A'
FROM items
WHERE name LIKE '%A';

/* 4. Mostrar los items que tengan relacionado el color Rojo */

SELECT i.name AS 'Item Rojo'
FROM items AS i
    INNER JOIN colors c ON i.colorId = c.id
WHERE c.name = 'ROJO';

/* 5. Se requiere asignar un precio a los items cuyo precio sea NULL,
 el precio a agregar debe ser calculado de la siguiente forma: costo del item + 10.000*/

UPDATE items
SET price = cost + 10000
WHERE price IS NULL OR price = 0;

/* 6. Incrementar el precio de los items en un 10% */

UPDATE items SET price = price + (price * 0.1);

/* 7. Consultar los items que comiencen con la letra "C" en el nombre, y anteponer la
 palabra "Nuevo" */

UPDATE items SET name = CONCAT('Nuevo ', name) WHERE name LIKE 'C%';

/* 8. Eliminar los items que pertenezcan a la compañía con ID #1 */

DELETE FROM items WHERE companyId = 1;

/* 9. Eliminar los items que tengan el costo menor a 10.000 */

DELETE FROM items WHERE cost < 10000;

/* 10. Cree una función que permita insertar registros en la tabla colores*/

INSERT INTO colors (code, name) VALUES
('9', 'PURPURA'),
('10', 'ROSA'),
('11', 'LAVANDA');

/* 11. Eliminar todos los datos de la tabla colores */

ALTER TABLE items DROP CONSTRAINT items_ibfk_1;

DELETE FROM colors;

/* 12. Agregar un campo llamado "description" en la tabla items, que permita ser NULL,
 y que tenga un máximo de 200 caracteres */

ALTER TABLE items ADD COLUMN description VARCHAR(200) NULL;
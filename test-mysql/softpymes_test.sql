CREATE database test_mysql;

USE test_mysql;

DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(25),
  `colorId` int null,
  `companyId` int,
  `cost` decimal,
  `price` decimal
);

DROP TABLE IF EXISTS `colors`;
CREATE TABLE `colors` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(3),
  `name` varchar(25)
);

DROP TABLE IF EXISTS `companies`;
CREATE TABLE `companies` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(3),
  `identificationNumber` varchar(15),
  `name` varchar(50)
);

ALTER TABLE `items` ADD FOREIGN KEY (`colorId`) REFERENCES `colors` (`id`);

ALTER TABLE `items` ADD FOREIGN KEY (`companyId`) REFERENCES `companies` (`id`);

LOCK TABLES `companies` WRITE;
INSERT INTO `companies` VALUES 
(null, '001', '123456789', 'SOFTPYMES'),
(null, '002', '654549864', 'ROSINA'),
(null, '003', '894151894', 'PHYSIOTRAUMA');
UNLOCK TABLES;

LOCK TABLES `colors` WRITE;
INSERT INTO `colors` VALUES
(null, '1', 'AZUL'),
(null, '2', 'ROJO'),
(null, '3', 'BLANCO'),
(null, '4', 'NEGRO'),
(null, '5', 'AMARILLO'),
(null, '6', 'VERDE'),
(null, '7', 'GRIS'),
(null, '8', 'NARANJA');
UNLOCK TABLES;

LOCK TABLES `items` WRITE;
INSERT INTO `items` VALUES
(null, 'ZAPATO', 5, 1, 6549, 0),
(null, 'CAMISA', 8, 2, 8976, 78218),
(null, 'PANTALON', 1, 3, 32156, 0),
(null, 'MEDIAS', 6, 1, 65198, 784151),
(null, 'VESTIDO', 2, 2, 32548, 0),
(null, 'GORRA', 5, 3, 894, 7884),
(null, 'SACO', 7, 1, 8943, 0),
(null, 'BUFANDA', 4, 2, 65494, 884151),
(null, 'ARAMARIO', 6, 3, 2316, 89451),
(null, 'NEVERA', 8, 1, 81651, 105143),
(null, 'ESTUFA', 5, 2, 3156, 9841),
(null, 'LAVADORA', 3, 3, 9840, 0),
(null, 'SILLON', 1, 1, 840, 5100),
(null, 'CAMA', 4, 2, 8942, 84151),
(null, 'COMEDOR', 7, 3, 3218, 6541151);
UNLOCK TABLES;

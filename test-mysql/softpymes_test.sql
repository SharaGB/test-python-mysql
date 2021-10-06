CREATE TABLE `items` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(25),
  `colorId` int null,
  `companyId` int,
  `price` decimal,
  `cost` decimal
);

CREATE TABLE `colors` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(3),
  `name` varchar(25)
);

CREATE TABLE `companies` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(3),
  `identificationNumber` varchar(15),
  `name` varchar(50)
);

ALTER TABLE `items` ADD FOREIGN KEY (`colorId`) REFERENCES `colors` (`id`);

ALTER TABLE `items` ADD FOREIGN KEY (`companyId`) REFERENCES `companies` (`id`);

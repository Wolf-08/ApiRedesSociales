-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.12-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for encuestas
CREATE DATABASE IF NOT EXISTS `encuestas` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `encuestas`;

-- Dumping structure for table encuestas.forms
CREATE TABLE IF NOT EXISTS `forms` (
  `email` varchar(50) DEFAULT NULL,
  `edad` varchar(2) DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `redFavorita` varchar(50) DEFAULT NULL,
  `TiempoFacebook` decimal(2,0) DEFAULT NULL,
  `TiempoInstagram` decimal(2,0) DEFAULT NULL,
  `TiempoTikTok` decimal(2,0) DEFAULT NULL,
  `TiempoWhatsapp` decimal(2,0) DEFAULT NULL,
  `TiempoTwitter` decimal(20,0) DEFAULT NULL,
  `id` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table encuestas.forms: ~8 rows (approximately)
/*!40000 ALTER TABLE `forms` DISABLE KEYS */;
INSERT INTO `forms` (`email`, `edad`, `sexo`, `redFavorita`, `TiempoFacebook`, `TiempoInstagram`, `TiempoTikTok`, `TiempoWhatsapp`, `TiempoTwitter`, `id`) VALUES
	('prueba3@gmail.com', '3', 'M', 'Wa', 2, 8, 3, 14, 6, 3),
	('kmarkwick9@fda.gov', '2', 'M', 'Wa', 10, 10, 10, 10, 10, 10),
	('kmaruick9@fda.gov', '4', 'M', 'Tk', 9, 10, 10, 10, 10, 11),
	('prueba5@gmail.com', '1', 'F', 'Tk', 0, 1, 4, 5, 0, 34),
	('prueba2@gmail.com', '2', 'F', 'Fa', 1, 6, 1, 3, 4, 36),
	('alejandro.montecillo@gmail.com', '1', 'M', 'Wa', 1, 3, 3, 1, 2, 45),
	('nataly@gmail.com', '1', 'F', 'Tk', 3, 5, 3, 3, 4, 46),
	('prueba6@gmail.com', '3', 'M', 'Wa', 3, 1, 5, 8, 14, 60);
/*!40000 ALTER TABLE `forms` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

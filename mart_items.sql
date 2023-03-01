-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: mart
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `item_code` int(11) NOT NULL DEFAULT '0',
  `product_name` varchar(50) DEFAULT NULL,
  `category` varchar(30) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (0,'(1)','(2)',3,4),(1001,'cornflakes','food',50,49),(1002,'bharti spices','food',100,65),(1003,'basmati rice','food',100,140),(1004,'dal','food',200,75),(1005,'biscuits','food',300,20),(1006,'tea','food',200,100),(1007,'coffee','food',200,150),(1008,'milk','food',100,30),(1009,'apple','food',30,150),(1010,'banana','food',30,40),(1011,'orange','food',30,50),(1012,'chips','food',100,20),(1013,'juice','food',50,100),(1014,'chocolate','food',200,150),(1015,'cold drink','food',200,40),(1016,'noodles','food',100,85),(1017,'pasta','food',100,25),(1018,'potato','food',100,45),(1019,'onion','food',100,100),(1020,'tomato','food',100,60),(1021,'cheese','food',50,180),(1022,'breads','food',50,40),(1023,'nuggets','food',200,140),(1024,'gulab jamun','food',50,110),(1025,'rasgulla','food',50,170),(1026,'ice cream','food',200,80),(1027,'hoodies','clothing',100,2000),(1028,'tshirts','clothing',300,400),(1029,'trousers','clothing',200,350),(1030,'pyjamas','clothing',300,500),(1031,'underwear','clothing',200,250),(1032,'shorts','clothing',300,400),(1033,'shirt','clothing',200,300),(1034,'socks','clothing',100,200),(1035,'slippers','clothing',100,250),(1036,'sandals','clothing',100,300),(1037,'formal shoes','clothing',100,2000),(1038,'sports shoes','clothing',200,1000),(1039,'bat','clothing',100,1500),(1040,'ball','clothing',300,200),(1041,'football','clothing',200,900),(1042,'basketball','clothing',200,500),(1043,'gear cycles','clothing',100,25000),(1044,'carrom','clothing',50,800),(1045,'badminton','clothing',100,400),(1046,'tennis','clothing',100,2500),(1047,'smartphones','electronics',200,10000),(1048,'tablets','electronics',200,20000),(1049,'bluetooth speakers','electronics',100,2000),(1050,'bluetooth headset','electronics',100,4000),(1051,'hd television','electronics',300,60000),(1052,'camera','electronics',200,40000),(1053,'playstation','electronics',100,30000),(1054,'gaming laptops','electronics',100,100000),(1055,'normal laptops','electronics',200,60000),(1056,'single door fridge','electronics',50,70000),(1057,'double door fridge','electronics',30,90000),(1058,'top load washing machine','electronics',20,30000),(1059,'front load washing machine','electronics',20,70000),(1060,'mixer grinder','electronics',50,5000),(1061,'led lights','electronics',200,1500),(1062,'pencil','stationary',100,150),(1063,'ink pen','stationary',200,70),(1064,'ball pen','stationary',200,20),(1065,'paints','stationary',100,200),(1066,'crayons','stationary',100,150),(1067,'eraser','stationary',200,10),(1068,'sharpener','stationary',200,15),(1069,'scale','stationary',100,30),(1070,'scissor','stationary',100,50),(1071,'stapler','stationary',100,80),(1072,'pendrives','electronics',100,800),(1073,'hard disks','electronics',100,8000),(1074,'trimmers','electronics',200,2000),(1075,'desktop pc','electronics',300,40000),(1076,'vaccum cleaner','electronics',100,50000),(1077,'earphones','electronics',200,1000),(1078,'speakers','electronics',300,9000),(1079,'game cd','electronics',500,2000),(1080,'split ac','electronics',200,40000),(1081,'window ac','electronics',200,20000),(1082,'room heater','electronics',300,10000),(1083,'keyboards','electronics',200,6000),(1084,'mouse','electronics',300,4000),(1085,'cake','food',200,300),(1086,'pizza','food',100,200),(1087,'pastry','food',200,90),(1088,'patties','food',300,60),(1089,'power bank','electronics',200,6000),(1090,'detergents','household chemicals',300,200),(1091,'soaps','household chemicals',300,150),(1092,'floor cleaners','household chemicals',100,300),(1093,'toilet cleaners','household chemicals',100,200),(1094,'shaving cream','household chemicals',100,100),(1095,'fairness cream','household chemicals',300,80),(1096,'deodrants','household chemicals',300,200),(1097,'makeup kit','household chemicals',200,2000),(1098,'razors','care',300,100),(1099,'toothbrush','care',300,80),(1100,'toothpaste','care',200,50);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-05 10:14:28

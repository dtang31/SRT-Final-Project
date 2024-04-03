-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: flaskapp
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flaskapp_reviews`
--

DROP TABLE IF EXISTS `flaskapp_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flaskapp_reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `User` varchar(255) DEFAULT 'Anonymous',
  `Car` varchar(255) NOT NULL,
  `Date` datetime NOT NULL,
  `Rating` varchar(5) NOT NULL,
  `Review` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flaskapp_reviews`
--

LOCK TABLES `flaskapp_reviews` WRITE;
/*!40000 ALTER TABLE `flaskapp_reviews` DISABLE KEYS */;
INSERT INTO `flaskapp_reviews` VALUES (1,'Cesar Jillan','Honda, Oddyssey, 2000.','2024-03-21 23:12:40','3','At first, I thought I would love vehicle. It was the perfect car for my cats. However, my cats keep getting stuck due to the car\'s poor design. Would not recommend.'),(2,'Anonymous','Toyata, Camry, 2004. ','2024-03-21 23:15:25','7','Fast Car! Great Car! What more can I say?'),(3,'Anonymous','Tesla, Model, 2024.','2024-03-21 23:29:11','10','Tesla is the best brand! Anything Tesla guarantees performance, quality and happiness! '),(4,'David Tang','Ford,  Escape, 2024.','2024-03-21 23:37:07','1','My friends always tell me that Ford is not a good brand. I was stupid and I didn\'t listen to them. Now I regret it, this is possibly the worst care I have ever had the displeasure of driving. Now I am debt and I need to sleep in it, RIP.'),(5,'Anonymous','BMW, X3, 2021.','2024-03-21 23:41:40','10','German Cars number 1 forever.'),(6,'Anonymous','Honda, Civic, 2023.','2024-03-21 23:45:04','7','I just wanted a cheap, reliable second car. This is more than sufficient for my needs. Comfortable! I love the monitor! Wish it was cleaner.'),(7,'Jenny Alice','Honda, Oddyssey, 2001.','2024-03-22 00:15:37','8','Quite good! I love going fast, I can accomplish that easily with this vehicle. Let\'s go! Vrooooooom!'),(8,'Alice Ma','Acura, MDX, 2024.','2024-03-22 02:57:29','8','I really really love love this car. This is the best car ever!!!!!!!!!!!!!!!!!!!!!!!!'),(9,'Fobby Bischer','Tesla, X3, 1999.','2024-03-22 14:39:20','10','I love the interiors of this vehicle. It\'s very high-tech. I feel like I am driving a space ship!'),(10,'Jamie J.','BMW, X3, 2024.','2024-03-22 14:40:44','9','I have never driven such an amazing vehicle! Good acceleration and speed! Great for long-trips! Great for family! '),(11,'Carrie Jischer','Kia, Stinger, 2023.','2024-03-22 14:59:54','3','I made one of the worst purchases in my life! This is a pain to drive. Screw Kia, I will never do business with them again.'),(12,'Anonymous','Toyota, Model, 2004.','2024-03-22 15:02:08','2','Just the worse! Second hand car, what can you expect? Everything is falling apart...'),(13,'Anonymous','Toyota, Camry, 1999.','2024-03-22 15:03:14','1','I decided to buy a 25 year old car. So yeah, it\'s bad. This car managed 3 km before it has broken down completely on the streets.'),(14,'Alexander Blate','BMW, X3, 2021.','2024-03-22 15:46:38','9','Decent vehicle! Strong horsepower!'),(15,'Anonymous','Acura, MDX, 2024.','2024-03-22 15:47:45','5','Acura just way too overpriced, what on earth were they thinking charging such a high premium for this junk.'),(16,'Jake Pall','Toyota, Camry, 1999.','2024-03-22 15:56:13','1','Do not waste your money on this. It fails in all categories across the board. If you buy it, be prepared to deal with endless repairs as pieces from the car will frequently break off. I wasted so much money repairing this car, I probably could have used that money to purchase a brand new car. Please don\'t make the same mistake I did. Value your spending, value your sanity!\r\n\r\nJake'),(17,'Jesus Oak','Honda, Odyssey, 2024.','2024-03-22 16:55:38','7','This is pretty large van. For my purposes, I wanted a large vehicle for my family of 8. My kids really like the back speakers and the entertainment system. The seats and the steering wheel are heated which makes them ideal for the winter.'),(18,'Bob Lance','Toyata, Sienna, 2009.','2024-03-22 17:35:31','2','This car is horrible, I hate it, my kids it hate, everybody hates it.'),(19,'Anonymous','Honda, X3, 1999.','2024-03-22 17:38:03','3','Some review, whatever');
/*!40000 ALTER TABLE `flaskapp_reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-22 17:54:02



#####Update DB structure #######
ALTER TABLE flaskapp_reviews add COLUMN `likecount` int NOT NULL;

-- MySQL dump 10.13  Distrib 9.4.0, for Win64 (x86_64)
--
-- Host: localhost    Database: storefront1
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `storefront1`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `storefront1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `storefront1`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Customer Service');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,33),(2,1,34),(3,1,35),(4,1,36),(5,1,45),(6,1,46),(7,1,47),(8,1,48),(9,1,53),(10,1,54),(11,1,55),(12,1,56);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add history entry',6,'add_historyentry'),(22,'Can change history entry',6,'change_historyentry'),(23,'Can delete history entry',6,'delete_historyentry'),(24,'Can view history entry',6,'view_historyentry'),(25,'Can add cart',7,'add_cart'),(26,'Can change cart',7,'change_cart'),(27,'Can delete cart',7,'delete_cart'),(28,'Can view cart',7,'view_cart'),(29,'Can add collection',8,'add_collection'),(30,'Can change collection',8,'change_collection'),(31,'Can delete collection',8,'delete_collection'),(32,'Can view collection',8,'view_collection'),(33,'Can add customer',9,'add_customer'),(34,'Can change customer',9,'change_customer'),(35,'Can delete customer',9,'delete_customer'),(36,'Can view customer',9,'view_customer'),(37,'Can add promotion',10,'add_promotion'),(38,'Can change promotion',10,'change_promotion'),(39,'Can delete promotion',10,'delete_promotion'),(40,'Can view promotion',10,'view_promotion'),(41,'Can add address',11,'add_address'),(42,'Can change address',11,'change_address'),(43,'Can delete address',11,'delete_address'),(44,'Can view address',11,'view_address'),(45,'Can add order',12,'add_order'),(46,'Can change order',12,'change_order'),(47,'Can delete order',12,'delete_order'),(48,'Can view order',12,'view_order'),(49,'Can add product',13,'add_product'),(50,'Can change product',13,'change_product'),(51,'Can delete product',13,'delete_product'),(52,'Can view product',13,'view_product'),(53,'Can add order item',14,'add_orderitem'),(54,'Can change order item',14,'change_orderitem'),(55,'Can delete order item',14,'delete_orderitem'),(56,'Can view order item',14,'view_orderitem'),(57,'Can add cart item',15,'add_cartitem'),(58,'Can change cart item',15,'change_cartitem'),(59,'Can delete cart item',15,'delete_cartitem'),(60,'Can view cart item',15,'view_cartitem'),(61,'Can add review',16,'add_review'),(62,'Can change review',16,'change_review'),(63,'Can delete review',16,'delete_review'),(64,'Can view review',16,'view_review'),(65,'Can add tag',17,'add_tag'),(66,'Can change tag',17,'change_tag'),(67,'Can delete tag',17,'delete_tag'),(68,'Can view tag',17,'view_tag'),(69,'Can add tagged items',18,'add_taggeditems'),(70,'Can change tagged items',18,'change_taggeditems'),(71,'Can delete tagged items',18,'delete_taggeditems'),(72,'Can view tagged items',18,'view_taggeditems'),(73,'Can add liked items',19,'add_likeditems'),(74,'Can change liked items',19,'change_likeditems'),(75,'Can delete liked items',19,'delete_likeditems'),(76,'Can view liked items',19,'view_likeditems'),(77,'Can add user',20,'add_user'),(78,'Can change user',20,'change_user'),(79,'Can delete user',20,'delete_user'),(80,'Can view user',20,'view_user'),(81,'Can cancel order',12,'cancel_order'),(82,'Can view history',9,'view_history'),(83,'Can add product image',21,'add_productimage'),(84,'Can change product image',21,'change_productimage'),(85,'Can delete product image',21,'delete_productimage'),(86,'Can view product image',21,'view_productimage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
INSERT INTO `core_user` VALUES (1,'pbkdf2_sha256$1000000$htPRqYgNTHTqfPPzbSZTms$v/ABYLzZDUQYizzsEG3iLYfiJUmVkIrtbZbRbj4iL1Y=','2025-09-30 15:00:02.442676',1,'admin','','',1,1,'2025-09-18 22:07:33.877076','otamendi1606@gmail.com'),(2,'pbkdf2_sha256$1000000$qsxL4NVnJmqk5SJ8idCOq8$boxuXtE2klKA9gDp4vaQ53a0rrmucHAuXMCRNSvG44A=','2025-09-23 12:55:48.000000',0,'LockInBoy','Lock','Boy',1,1,'2025-09-18 22:12:47.000000','otamendi1606+django@gmail.com'),(3,'pbkdf2_sha256$1000000$ujsKK18GA16gCzldM0okSo$G9wxC43gRqffir2AfmsB5tksXUdHpLMIXCQyFpknDDE=',NULL,0,'domainman','Jamil','Jaman',0,1,'2025-09-19 11:00:28.000000','user1@domain.com'),(4,'pbkdf2_sha256$1000000$ERYydSOHqEOIWAQIivhVIn$q0tw3yAeh9XZufvpTW9NSSKf1a5YW+49zKYc22zsuZk=',NULL,0,'user2','User','Nwa mama',0,1,'2025-09-19 11:07:48.720383','user2@domain.com'),(5,'pbkdf2_sha256$1000000$WcrkfVwxnDt3tVKI44g43j$8+gYCI8Svr0vlCBY0NjBgHuwZlINmQHyYxkXmQHdGGI=',NULL,0,'user3','User3','Nwa mamas',0,1,'2025-09-19 12:23:54.456885','user3@domain.com'),(6,'',NULL,0,'jdoe','John','Doe',0,1,'2025-09-23 14:29:28.000000','john@example.com'),(7,'',NULL,0,'asmith','Alice','Smith',0,1,'2025-09-23 14:29:28.000000','alice@example.com'),(8,'',NULL,0,'bwayne','Bruce','Wayne',0,1,'2025-09-23 14:29:28.000000','bruce@example.com'),(9,'pbkdf2_sha256$1000000$crA2TuuoYAdG76HSGCvTVF$FXlNz8vXtGYGyAyYIMOthsXNh9CkmCZGBANBPGe4ToY=',NULL,0,'Signal','Signal','Iduna',0,1,'2025-09-26 11:12:33.210433','signal@domain.com');
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
INSERT INTO `core_user_groups` VALUES (1,2,1);
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
INSERT INTO `core_user_user_permissions` VALUES (1,2,81),(2,2,82);
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `debug_toolbar_historyentry`
--

DROP TABLE IF EXISTS `debug_toolbar_historyentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `debug_toolbar_historyentry` (
  `request_id` char(32) NOT NULL,
  `data` json NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `debug_toolbar_historyentry`
--

LOCK TABLES `debug_toolbar_historyentry` WRITE;
/*!40000 ALTER TABLE `debug_toolbar_historyentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `debug_toolbar_historyentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-09-18 22:12:49.649732','2','LockInBoy',1,'[{\"added\": {}}]',20,1),(2,'2025-09-18 22:26:17.022237','1',' ',1,'[{\"added\": {}}]',9,1),(3,'2025-09-18 22:26:28.794945','2','Lock Boy',1,'[{\"added\": {}}]',9,1),(4,'2025-09-18 22:31:32.520152','1','Customer Service',1,'[{\"added\": {}}]',3,1),(5,'2025-09-18 22:32:01.280218','2','LockInBoy',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',20,1),(6,'2025-09-19 17:28:47.683117','3','domainman',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',20,1),(7,'2025-09-23 12:57:34.151579','2','LockInBoy',2,'[{\"changed\": {\"fields\": [\"User permissions\"]}}]',20,1),(8,'2025-09-23 14:06:02.157112','2','LockInBoy',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',20,1),(9,'2025-09-26 10:47:23.780803','2','LockInBoy',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',20,1),(10,'2025-09-26 11:17:56.314203','9','Signal',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',20,1),(11,'2025-09-30 14:30:28.213783','1','tagito',1,'[{\"added\": {}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(20,'core','user'),(6,'debug_toolbar','historyentry'),(19,'likes','likeditems'),(5,'sessions','session'),(11,'store','address'),(7,'store','cart'),(15,'store','cartitem'),(8,'store','collection'),(9,'store','customer'),(12,'store','order'),(14,'store','orderitem'),(13,'store','product'),(21,'store','productimage'),(10,'store','promotion'),(16,'store','review'),(17,'tags','tag'),(18,'tags','taggeditems');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-09-18 22:06:14.415589'),(2,'contenttypes','0002_remove_content_type_name','2025-09-18 22:06:14.565652'),(3,'auth','0001_initial','2025-09-18 22:06:14.965902'),(4,'auth','0002_alter_permission_name_max_length','2025-09-18 22:06:15.058150'),(5,'auth','0003_alter_user_email_max_length','2025-09-18 22:06:15.065098'),(6,'auth','0004_alter_user_username_opts','2025-09-18 22:06:15.071211'),(7,'auth','0005_alter_user_last_login_null','2025-09-18 22:06:15.077047'),(8,'auth','0006_require_contenttypes_0002','2025-09-18 22:06:15.079294'),(9,'auth','0007_alter_validators_add_error_messages','2025-09-18 22:06:15.085396'),(10,'auth','0008_alter_user_username_max_length','2025-09-18 22:06:15.093431'),(11,'auth','0009_alter_user_last_name_max_length','2025-09-18 22:06:15.100290'),(12,'auth','0010_alter_group_name_max_length','2025-09-18 22:06:15.127003'),(13,'auth','0011_update_proxy_permissions','2025-09-18 22:06:15.136023'),(14,'auth','0012_alter_user_first_name_max_length','2025-09-18 22:06:15.144621'),(15,'core','0001_initial','2025-09-18 22:06:15.624821'),(16,'admin','0001_initial','2025-09-18 22:06:15.853961'),(17,'admin','0002_logentry_remove_auto_add','2025-09-18 22:06:15.862408'),(18,'admin','0003_logentry_add_action_flag_choices','2025-09-18 22:06:15.872521'),(19,'debug_toolbar','0001_initial','2025-09-18 22:06:15.897898'),(20,'likes','0001_initial','2025-09-18 22:06:16.106008'),(21,'sessions','0001_initial','2025-09-18 22:06:16.170592'),(22,'store','0001_initial','2025-09-18 22:06:17.322656'),(23,'store','0002_review','2025-09-18 22:06:17.444818'),(24,'store','0003_alter_cart_id','2025-09-18 22:06:17.817080'),(25,'store','0004_alter_cartitem_cart_alter_cartitem_unique_together','2025-09-18 22:06:17.865413'),(26,'store','0005_alter_cartitem_quantity','2025-09-18 22:06:17.954713'),(27,'tags','0001_initial','2025-09-18 22:06:18.184068'),(28,'store','0006_alter_customer_options_remove_customer_email_and_more','2025-09-18 22:24:23.892810'),(29,'store','0007_alter_order_options','2025-09-18 22:36:36.705307'),(30,'store','0008_alter_customer_options','2025-09-23 12:42:11.687413'),(31,'store','0009_alter_orderitem_order','2025-09-26 12:09:36.664962'),(32,'store','0010_productimage','2025-09-26 12:39:42.146337'),(33,'store','0011_alter_productimage_image','2025-09-29 09:49:19.079151');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('c5rakku7z2gtxhddtxprfwyc0qz4951z','.eJxVjEEOwiAQRe_C2hBgDBSX7j0DmWGmUjWQlHZlvLtt0oVu33v_v1XCdSlp7TKnidVFWXX6ZYT5KXUX_MB6bzq3uswT6T3Rh-361lhe16P9OyjYy7Y2cPaWDNggwJjFjgDRMFkaHLFHMhIpRMgULfmRvEAwG_RxYJeNU58v5JM4FQ:1v3bpi:QhALP6_GRjziy_nGdWyEHlZwUQT3KVvcSdw4Xrs2mNw','2025-10-14 15:00:02.463974');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes_likeditems`
--

DROP TABLE IF EXISTS `likes_likeditems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes_likeditems` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `object_id` int unsigned NOT NULL,
  `content_type_id` int NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `likes_likeditems_content_type_id_a760afd3_fk_django_co` (`content_type_id`),
  KEY `likes_likeditems_user_id_5b6055e6_fk_core_user_id` (`user_id`),
  CONSTRAINT `likes_likeditems_content_type_id_a760afd3_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `likes_likeditems_user_id_5b6055e6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `likes_likeditems_chk_1` CHECK ((`object_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes_likeditems`
--

LOCK TABLES `likes_likeditems` WRITE;
/*!40000 ALTER TABLE `likes_likeditems` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes_likeditems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_address`
--

DROP TABLE IF EXISTS `store_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `zip_code` varchar(20) NOT NULL,
  `country` varchar(255) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_address_customer_id_080cf871_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_address_customer_id_080cf871_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_address`
--

LOCK TABLES `store_address` WRITE;
/*!40000 ALTER TABLE `store_address` DISABLE KEYS */;
INSERT INTO `store_address` VALUES (1,'123 Main St','New York','10001','USA',1),(2,'456 High St','London','SW1A','UK',2);
/*!40000 ALTER TABLE `store_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_cart`
--

DROP TABLE IF EXISTS `store_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_cart` (
  `id` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_cart`
--

LOCK TABLES `store_cart` WRITE;
/*!40000 ALTER TABLE `store_cart` DISABLE KEYS */;
INSERT INTO `store_cart` VALUES ('3a227072450d4df19d403a474dfe82a0','2025-09-23 14:32:02.968988'),('3ecca00ba8454da19f02167859d4ea36','2025-09-26 10:36:27.592155'),('7e6b1c70d2304357a306e66a2e067592','2025-09-26 11:32:55.418567'),('c63988957803456a806c36229c73fe7e','2025-09-23 18:01:34.568835');
/*!40000 ALTER TABLE `store_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_cartitem`
--

DROP TABLE IF EXISTS `store_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint unsigned NOT NULL,
  `cart_id` char(32) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `store_cartitem_cart_id_product_id_bd38e607_uniq` (`cart_id`,`product_id`),
  KEY `store_cartitem_product_id_4238d443_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_cartitem_cart_id_4f60ac05_fk` FOREIGN KEY (`cart_id`) REFERENCES `store_cart` (`id`),
  CONSTRAINT `store_cartitem_product_id_4238d443_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`),
  CONSTRAINT `store_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_cartitem`
--

LOCK TABLES `store_cartitem` WRITE;
/*!40000 ALTER TABLE `store_cartitem` DISABLE KEYS */;
INSERT INTO `store_cartitem` VALUES (1,10,'c63988957803456a806c36229c73fe7e',1),(2,60,'c63988957803456a806c36229c73fe7e',2);
/*!40000 ALTER TABLE `store_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_collection`
--

DROP TABLE IF EXISTS `store_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_collection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `featured_product_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `store_collection_featured_product_id_001d6455_fk_store_pro` (`featured_product_id`),
  CONSTRAINT `store_collection_featured_product_id_001d6455_fk_store_pro` FOREIGN KEY (`featured_product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_collection`
--

LOCK TABLES `store_collection` WRITE;
/*!40000 ALTER TABLE `store_collection` DISABLE KEYS */;
INSERT INTO `store_collection` VALUES (1,'Electronics',NULL),(2,'Clothing',NULL),(3,'Books',NULL),(4,'Toys',NULL);
/*!40000 ALTER TABLE `store_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_customer`
--

DROP TABLE IF EXISTS `store_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone` varchar(60) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `membership` varchar(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `store_customer_user_id_04276401_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_customer`
--

LOCK TABLES `store_customer` WRITE;
/*!40000 ALTER TABLE `store_customer` DISABLE KEYS */;
INSERT INTO `store_customer` VALUES (1,'345','2025-10-06','B',1),(2,'245',NULL,'S',2),(3,'2356','2019-06-19','B',5),(4,'23442344','2025-09-23','S',4),(5,'1234567890','1990-05-10','G',6),(6,'2345678901','1985-07-20','S',7),(7,'3456789012','1975-11-30','B',8),(8,'345','2025-09-09','G',9);
/*!40000 ALTER TABLE `store_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_order`
--

DROP TABLE IF EXISTS `store_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `placed_at` datetime(6) NOT NULL,
  `payment_status` varchar(1) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_order_customer_id_13d6d43e_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_order_customer_id_13d6d43e_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_order`
--

LOCK TABLES `store_order` WRITE;
/*!40000 ALTER TABLE `store_order` DISABLE KEYS */;
INSERT INTO `store_order` VALUES (1,'2025-09-23 14:39:02.000000','p',3),(2,'2025-09-23 14:40:51.000000','P',2),(3,'2025-09-23 17:21:30.213956','P',2),(4,'2025-09-23 18:01:12.985181','C',2),(5,'2025-09-23 18:02:55.753712','P',2),(6,'2025-09-26 10:12:54.810553','C',2),(7,'2025-09-26 10:18:40.680314','P',2),(8,'2025-09-26 10:18:55.659706','P',2),(9,'2025-09-26 10:33:29.971129','P',2);
/*!40000 ALTER TABLE `store_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_orderitem`
--

DROP TABLE IF EXISTS `store_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint NOT NULL,
  `unit_price` decimal(6,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_orderitem_order_id_acf8722d_fk_store_order_id` (`order_id`),
  KEY `store_orderitem_product_id_f2b098d4_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_orderitem_order_id_acf8722d_fk_store_order_id` FOREIGN KEY (`order_id`) REFERENCES `store_order` (`id`),
  CONSTRAINT `store_orderitem_product_id_f2b098d4_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_orderitem`
--

LOCK TABLES `store_orderitem` WRITE;
/*!40000 ALTER TABLE `store_orderitem` DISABLE KEYS */;
INSERT INTO `store_orderitem` VALUES (1,1,699.99,1,1),(2,2,199.99,1,5),(3,3,19.99,2,3),(4,10,699.99,5,1),(5,60,1299.99,5,2);
/*!40000 ALTER TABLE `store_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_product`
--

DROP TABLE IF EXISTS `store_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext,
  `unit_price` decimal(6,2) NOT NULL,
  `inventory` int NOT NULL,
  `last_update` datetime(6) NOT NULL,
  `collections_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `store_product_collections_id_dd655a77_fk_store_collection_id` (`collections_id`),
  CONSTRAINT `store_product_collections_id_dd655a77_fk_store_collection_id` FOREIGN KEY (`collections_id`) REFERENCES `store_collection` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_product`
--

LOCK TABLES `store_product` WRITE;
/*!40000 ALTER TABLE `store_product` DISABLE KEYS */;
INSERT INTO `store_product` VALUES (1,'Smartphone','smartphone','Latest smartphone',699.99,50,'2025-09-23 14:34:20.000000',1),(2,'Laptop','laptop','Gaming laptop',1299.99,20,'2025-09-23 14:34:20.000000',1),(3,'T-Shirt','tshirt','Cotton T-Shirt',19.99,200,'2025-09-23 14:34:20.000000',2),(4,'Novel','novel','Bestseller book',12.99,150,'2025-09-23 14:34:20.000000',3),(5,'Headphones','headphones','Noise-cancelling',199.99,80,'2025-09-23 14:34:20.000000',1),(6,'Woody Bone','woody-bone','Woody\'s toy story bone',39.45,4,'2025-09-26 12:23:08.003561',4);
/*!40000 ALTER TABLE `store_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_product_promotions`
--

DROP TABLE IF EXISTS `store_product_promotions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_product_promotions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_id` bigint NOT NULL,
  `promotion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `store_product_promotions_product_id_promotion_id_d02f5543_uniq` (`product_id`,`promotion_id`),
  KEY `store_product_promot_promotion_id_4bd05cf2_fk_store_pro` (`promotion_id`),
  CONSTRAINT `store_product_promot_promotion_id_4bd05cf2_fk_store_pro` FOREIGN KEY (`promotion_id`) REFERENCES `store_promotion` (`id`),
  CONSTRAINT `store_product_promotions_product_id_c302ec3a_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_product_promotions`
--

LOCK TABLES `store_product_promotions` WRITE;
/*!40000 ALTER TABLE `store_product_promotions` DISABLE KEYS */;
INSERT INTO `store_product_promotions` VALUES (1,1,1),(2,2,2),(3,5,1);
/*!40000 ALTER TABLE `store_product_promotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_productimage`
--

DROP TABLE IF EXISTS `store_productimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_productimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_productimage_product_id_e50e4046_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_productimage_product_id_e50e4046_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_productimage`
--

LOCK TABLES `store_productimage` WRITE;
/*!40000 ALTER TABLE `store_productimage` DISABLE KEYS */;
INSERT INTO `store_productimage` VALUES (1,'store/images/cat_cIjH96b.jpeg',1),(2,'store/images/headphones.jpg',5),(3,'store/images/cat_g5obIkF.jpeg',6),(4,'store/images/cat_L5rEeoK.jpeg',1),(5,'store/images/cat_UIYeg5L.jpeg',1),(6,'store/images/headphones_7R1e6xN.jpg',1),(7,'store/images/headphones_fIOupeu.jpg',1);
/*!40000 ALTER TABLE `store_productimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_promotion`
--

DROP TABLE IF EXISTS `store_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_promotion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `discount` decimal(5,2) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_promotion`
--

LOCK TABLES `store_promotion` WRITE;
/*!40000 ALTER TABLE `store_promotion` DISABLE KEYS */;
INSERT INTO `store_promotion` VALUES (1,'Summer Sale',10.00,'2025-09-23 14:34:00.000000','2025-10-23 14:34:00.000000'),(2,'Black Friday',25.00,'2025-09-23 14:34:00.000000','2025-10-03 14:34:00.000000');
/*!40000 ALTER TABLE `store_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_review`
--

DROP TABLE IF EXISTS `store_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_review_product_id_abc413b2_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_review_product_id_abc413b2_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_review`
--

LOCK TABLES `store_review` WRITE;
/*!40000 ALTER TABLE `store_review` DISABLE KEYS */;
INSERT INTO `store_review` VALUES (1,'Alice','Great phone!','2025-09-23',1),(2,'Bruce','Loved the story','2025-09-23',4);
/*!40000 ALTER TABLE `store_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags_tag`
--

DROP TABLE IF EXISTS `tags_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `label` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags_tag`
--

LOCK TABLES `tags_tag` WRITE;
/*!40000 ALTER TABLE `tags_tag` DISABLE KEYS */;
INSERT INTO `tags_tag` VALUES (1,'tagito'),(2,'New Tag');
/*!40000 ALTER TABLE `tags_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags_taggeditems`
--

DROP TABLE IF EXISTS `tags_taggeditems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags_taggeditems` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `object_id` int unsigned NOT NULL,
  `content_type_id` int NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tags_taggeditems_content_type_id_ca691a60_fk_django_co` (`content_type_id`),
  KEY `tags_taggeditems_tag_id_35646fbc_fk_tags_tag_id` (`tag_id`),
  CONSTRAINT `tags_taggeditems_content_type_id_ca691a60_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `tags_taggeditems_tag_id_35646fbc_fk_tags_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `tags_tag` (`id`),
  CONSTRAINT `tags_taggeditems_chk_1` CHECK ((`object_id` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags_taggeditems`
--

LOCK TABLES `tags_taggeditems` WRITE;
/*!40000 ALTER TABLE `tags_taggeditems` DISABLE KEYS */;
INSERT INTO `tags_taggeditems` VALUES (1,5,13,2);
/*!40000 ALTER TABLE `tags_taggeditems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-02  8:35:43

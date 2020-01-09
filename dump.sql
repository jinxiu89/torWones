-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: wones
-- ------------------------------------------------------
-- Server version	5.7.22-log

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('59f53f8f5831');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_foreign_oauth`
--

DROP TABLE IF EXISTS `tb_foreign_oauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_foreign_oauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `oauth_name` varchar(32) DEFAULT NULL,
  `oauth_id` int(11) DEFAULT NULL,
  `access_token` varchar(64) DEFAULT NULL,
  `oauth_expires` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `tb_foreign_oauth_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_foreign_oauth`
--

LOCK TABLES `tb_foreign_oauth` WRITE;
/*!40000 ALTER TABLE `tb_foreign_oauth` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_foreign_oauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_local_oauth`
--

DROP TABLE IF EXISTS `tb_local_oauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_local_oauth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `tb_local_oauth_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_local_oauth`
--

LOCK TABLES `tb_local_oauth` WRITE;
/*!40000 ALTER TABLE `tb_local_oauth` DISABLE KEYS */;
INSERT INTO `tb_local_oauth` VALUES (1,1,'$p5k2$2537$q0pnzXdU$QU/M.CQt3UNvevN5SUy3GXhLw/Ei3W1O'),(2,2,'$p5k2$2537$n.YxIUS2$Ry8HfH.oCSJLxGdc61gksMIcX/JYAgfB'),(3,3,'$p5k2$2537$MNAKq99F$WmbP8NowG6f6t4ax3dMxDYiZHdtw8mUA'),(4,4,'$p5k2$2537$hSs2ZeDy$nonAulqoFj9TbL5eIxDWQ9vIox6VRH8t');
/*!40000 ALTER TABLE `tb_local_oauth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_permission`
--

DROP TABLE IF EXISTS `tb_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `handler` varchar(64) NOT NULL,
  `description` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `tb_permission_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `tb_permission_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_permission`
--

LOCK TABLES `tb_permission` WRITE;
/*!40000 ALTER TABLE `tb_permission` DISABLE KEYS */;
INSERT INTO `tb_permission` VALUES (1,'管理员管理',1,'/passport/account.html','管理员列表，用于管理管理员'),(2,'权限组管理',1,'permissionHandlers.PermissionGroup','用于权限组的管理'),(3,'权限管理',1,'/passport/permissions','用于管理权限，添加权限，开发完成后本功能隐藏'),(4,'角色管理列表',2,'/passport/roles12','查阅有哪些角色'),(5,'测试权限',2,'handler/add','测试权限,测试权限'),(6,'测试权限3',2,'shopHandler/add_shoping','购物车管理，添加删除'),(7,'角色列表',1,'/passport/roles','查看角色列表'),(8,'administrator',2,'shopHandler/add_shoping','超级用户，可以干除了删除网站的一'),(9,'权限编辑权限',1,'/passport/permissions/edit/\\d+','是否有编辑权限'),(10,'权限组添加',1,'permissionHandlers.AddPermissionGroup','添加权限组权限'),(11,'编辑权限组',1,'permissionHandlers.EditPermissionGroup','编辑权限组权限'),(12,'添加权限',1,'/passport/permissions/add/(?P<group_id>[0-9]+)','添加权限的权限'),(13,'角色添加',1,'/passport/role/add','添加角色权限'),(14,'编辑角色',1,'/passport/role/edit/(?P<role_id>[0-9]+)','编辑角色权限'),(15,'设置角色权限',1,'/passport/roles/set/permission/[0-9]+','设置角色权限'),(16,'添加用户',1,'/passport/account/user/add/','添加用户权限'),(17,'编辑用户权限',1,'/passport/account/user/edit/(?P<user_id>[0-9]+)','编辑用户权限'),(18,'设置用户角色',1,'/passport/account/user/set/role/(?P<user_id>[0-9]+)','设置用户角色'),(19,'设置为超级用户',1,'/passport/account/user/set/admin/(?P<user_id>[0-9]+)','设置为超级用户');
/*!40000 ALTER TABLE `tb_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_permission_group`
--

DROP TABLE IF EXISTS `tb_permission_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_permission_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `description` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_permission_group`
--

LOCK TABLES `tb_permission_group` WRITE;
/*!40000 ALTER TABLE `tb_permission_group` DISABLE KEYS */;
INSERT INTO `tb_permission_group` VALUES (1,'管理员模块','管理员模块'),(2,'管理员组','编辑器，可以提供编辑权限1');
/*!40000 ALTER TABLE `tb_permission_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_permission_handler`
--

DROP TABLE IF EXISTS `tb_permission_handler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_permission_handler` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  CONSTRAINT `tb_permission_handler_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `tb_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_permission_handler`
--

LOCK TABLES `tb_permission_handler` WRITE;
/*!40000 ALTER TABLE `tb_permission_handler` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_permission_handler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_permission_menu`
--

DROP TABLE IF EXISTS `tb_permission_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_permission_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  CONSTRAINT `tb_permission_menu_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `tb_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_permission_menu`
--

LOCK TABLES `tb_permission_menu` WRITE;
/*!40000 ALTER TABLE `tb_permission_menu` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_permission_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_permission_role`
--

DROP TABLE IF EXISTS `tb_permission_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_permission_role` (
  `permission_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`permission_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `tb_permission_role_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `tb_permission` (`id`),
  CONSTRAINT `tb_permission_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `tb_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_permission_role`
--

LOCK TABLES `tb_permission_role` WRITE;
/*!40000 ALTER TABLE `tb_permission_role` DISABLE KEYS */;
INSERT INTO `tb_permission_role` VALUES (1,2),(2,2),(3,2),(7,2),(9,2),(10,2),(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,2),(18,2),(19,2),(2,3),(3,3),(4,3),(2,4),(4,4),(1,5),(2,5),(3,5),(4,5),(1,6),(2,6),(3,6),(4,6);
/*!40000 ALTER TABLE `tb_permission_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_product`
--

DROP TABLE IF EXISTS `tb_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL COMMENT 'url_标题',
  `description` varchar(128) DEFAULT NULL COMMENT 'SKU描述',
  `keywords` varchar(128) DEFAULT NULL COMMENT '关键词',
  `name` varchar(128) DEFAULT NULL COMMENT '产品标题',
  `price` decimal(10,2) DEFAULT NULL COMMENT '商品最低价格,保留2位小数',
  `rating` float DEFAULT NULL COMMENT '商品评分',
  `review_count` int(11) DEFAULT NULL COMMENT '评论数量',
  `sales_volume` int(11) DEFAULT NULL COMMENT '销售量',
  `status` smallint(6) DEFAULT NULL COMMENT '是否在售',
  `thumbnail` varchar(255) DEFAULT NULL COMMENT '缩略图',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_product`
--

LOCK TABLES `tb_product` WRITE;
/*!40000 ALTER TABLE `tb_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_product_sku`
--

DROP TABLE IF EXISTS `tb_product_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_product_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL COMMENT '产品关联键',
  `name` varchar(128) DEFAULT NULL COMMENT 'SKU名称',
  `description` varchar(128) DEFAULT NULL COMMENT 'SKU描述',
  `price` decimal(10,2) DEFAULT NULL COMMENT 'SKU价格',
  `stock` int(11) DEFAULT NULL COMMENT 'SKU库存',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_product_sku`
--

LOCK TABLES `tb_product_sku` WRITE;
/*!40000 ALTER TABLE `tb_product_sku` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_product_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_role`
--

DROP TABLE IF EXISTS `tb_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `description` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_role`
--

LOCK TABLES `tb_role` WRITE;
/*!40000 ALTER TABLE `tb_role` DISABLE KEYS */;
INSERT INTO `tb_role` VALUES (2,'管理员管理','可以管理管理员模块'),(3,'wavlink','超级用户，可以干除了删除网站的一切权限'),(4,'keball','超级用户，可以干除了删除网站的一切权限'),(5,'国家管理员','可以添加国家管理，abcde'),(6,'网站管理员','网站管理员能管理用户，以及安全配');
/*!40000 ALTER TABLE `tb_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user_role`
--

DROP TABLE IF EXISTS `tb_user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `tb_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `tb_role` (`id`),
  CONSTRAINT `tb_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `tb_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user_role`
--

LOCK TABLES `tb_user_role` WRITE;
/*!40000 ALTER TABLE `tb_user_role` DISABLE KEYS */;
INSERT INTO `tb_user_role` VALUES (1,2),(2,2),(1,3),(1,4);
/*!40000 ALTER TABLE `tb_user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_users`
--

DROP TABLE IF EXISTS `tb_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(64) NOT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `qq` varchar(13) DEFAULT NULL,
  `_locked` tinyint(1) NOT NULL,
  `_is_delete` tinyint(1) NOT NULL,
  `_avatar` varchar(128) DEFAULT NULL,
  `is_admin` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_users`
--

LOCK TABLES `tb_users` WRITE;
/*!40000 ALTER TABLE `tb_users` DISABLE KEYS */;
INSERT INTO `tb_users` VALUES (1,'c093eef1-dc89-4881-a113-a6cdedc53cb2','kevin','qiu','2019-03-24 10:38:09','jinxiu89@163.com','13425131043','2447376396',0,0,NULL,1),(2,'6117dc34-967b-4d62-8a9b-e7af9208c01d','admin','admin','2019-03-24 10:47:19','system@win-star.com','18948330643','2447376396',0,0,NULL,1),(3,'5a1928ec-d2bf-4302-b7e1-d0e71043fcdc','keball','keball','2019-03-24 10:47:19','jinxiu89@163.com','13425131043','2447376396',0,0,NULL,NULL),(4,'b03919cf-8b17-4b7f-93fb-27f886ac5a7d','wavlink','wavlink','2019-03-24 10:50:28','system@win-star.com','18948330643','2447376396',0,0,NULL,NULL);
/*!40000 ALTER TABLE `tb_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-09 20:13:28

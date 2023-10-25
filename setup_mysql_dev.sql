-- This script creates a MySQL server with:
-- A database called hbnb_dev_db.
-- A new user called hbnb_dev with password hbnb_dev_pwd.
-- Grants all privileges for hbnb_dev on hbnb_dev_db.
-- Grants SELECT privilege for hbnb_dev on performance_schema.
-- All privileges only for this database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

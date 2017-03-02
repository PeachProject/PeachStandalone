CREATE DATABASE IF NOT EXISTS peach;
CREATE USER IF NOT EXISTS 'peach'@'localhost' IDENTIFIED BY 'peachuser';
GRANT ALL PRIVILEGES ON * . * TO 'peach'@'localhost';
FLUSH PRIVILEGES;
use peach;

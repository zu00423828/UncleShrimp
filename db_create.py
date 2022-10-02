import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


def get_db_setting():
    db_host = os.environ.get('DBHOST')
    db_port = os.environ.get('DBPORT')
    db_user = os.environ.get('DBUSER')
    db_passwd = os.environ.get('DBPASSWD')
    db_name = os.environ.get('DBNAME')
    return db_host, db_port, db_user, db_passwd, db_name


db_host, db_port, db_user, db_passwd, db_name = get_db_setting()

user = '''   
    CREATE TABLE IF NOT EXISTS `user` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `account` CHAR(128) NOT NULL,
    `password` CHAR(64) NOT NULL,
    `admin` BOOLEAN NOT NULL DEFAULT FALSE,
    `name` CHAR(32) NOT NULL,
    `phone` CHAR(15) NOT NULL, 
    `address`TEXT NOT NULL,
    `create_datetime` DATETIME NOT NULL,
    UNIQUE KEY `uniq_account` (account(128))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
auth = '''
    CREATE TABLE IF NOT EXISTS `auth` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `user_id` INTEGER NOT NULL,
    `token` CHAR(128) NOT NULL,
    expiration_datetime DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
product = '''   
    CREATE TABLE IF NOT EXISTS `product` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `name` CHAR(128) NOT NULL,
    `image` LONGBLOB NOT NULL,
    `quantity` INTEGER NOT NULL,
    `price` INTEGER NULL,
    `depiction` TEXT NOT NULL,
    `display` BOOLEAN NOT NULL,
    `create_datetime` DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
order = '''CREATE TABLE IF NOT EXISTS `order` (
`id` INTEGER PRIMARY KEY AUTO_INCREMENT,
`user_id` INTEGER NOT NULL,
`info` TEXT NOT NULL, 
`total` INTEGER NOT NULL,
`status` ENUM('unconfirmed','not shipped','shipped','finish') NOT NULL,
`create_datetime` DATETIME NOT NULL,
FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
# shopcart = '''CREATE TABLE IF NOT EXISTS `order` (
# `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
# `user_id` INTEGER NOT NULL,
# `total` INTEGER NOT NULL,
# `status` ENUM('Not shipped','Shipped','finish') NOT NULL
# FOREIGN KEY(client_id) REFERENCES client(id) ON DELETE CASCADE ON UPDATE CASCADE,
# '''


def create_db():
    conn = pymysql.connect(host=db_host, user=db_user,
                           password=db_passwd,)
    cur = conn.cursor()
    cur.execute(
        "CREATE DATABASE IF NOT EXISTS uncleshrimp CHARACTER SET utf8 COLLATE utf8_general_ci")
    conn.commit()
    conn.close()
    conn = pymysql.connect(host=db_host, user=db_user,
                           password=db_passwd, database=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute(user)
    cur.execute(auth)
    cur.execute(product)
    cur.execute(order)
    conn.commit()


if __name__ == '__main__':
    create_db()

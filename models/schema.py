import pymysql
user = '''   
    CREATE TABLE IF NOT EXISTS `user` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `account` CHAR(128) NOT NULL,
    `salt` CHAR(32) NOT NULL,
    `pwd` CHAR(64) NOT NULL,
    `admin` BOOLEAN NOT NULL DEFAULT FALSE,
    `name` CHAR(32) NOT NULL,
    `phone` CHAR(15) NOT NULL, 
    `address`TEXT NOT NULL,
    `create_datetime` DATETIME NOT NULL,
    UNIQUE KEY `uniq_salt` (salt(32)),
    UNIQUE KEY `uniq_account` (account(128))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''

product = '''   
    CREATE TABLE IF NOT EXISTS `product` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `name` CHAR(128) NOT NULL,
    `imge` LONGBLOB NOT NULL,
    `quantity` INTEGER NOT NULL,
    `price` INTEGER NULL,
    `create_datetime` DATETIME NOT NULL,
    `depiction` TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
order = '''CREATE TABLE IF NOT EXISTS `order` (
`id` INTEGER PRIMARY KEY AUTO_INCREMENT,
`user_id` INTEGER NOT NULL,
`total` INTEGER NOT NULL,
`create_datetime` DATETIME NOT NULL,
`status` ENUM('Not shipped','Shipped','finish') NOT NULL,
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
    conn = pymysql.connect(host='localhost', user='root',
                           password='zu7957232',)
    cur = conn.cursor()
    cur.execute(
        "CREATE DATABASE IF NOT EXISTS uncleshrimp CHARACTER SET utf8 COLLATE utf8_general_ci")
    conn.commit()
    conn.close()
    conn = pymysql.connect(host='localhost', user='root',
                           password='zu7957232', database='uncleshrimp', charset="utf8")
    cur = conn.cursor()
    cur.execute(user)
    cur.execute(product)
    cur.execute(order)
    conn.commit()


if __name__ == '__main__':
    create_db()

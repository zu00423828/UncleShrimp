user = '''   
    CREATE TABLE IF NOT EXISTS `user` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
    `account` CHAR(128) NOT NULL,
    `salt` CHAR(32) NOT NULL,
    `pwd` CHAR(64) NOT NULL,
    `admin` BOOLEN NOT NULL DEFAULT FALSE,
    `create_datetime` DATETIME NOT NULL,
    `comment` TEXT NULL,
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
    `depiction` TEXT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
'''
order = '''CREATE TABLE IF NOT EXISTS `order` (
`id` INTEGER PRIMARY KEY AUTO_INCREMENT,
`user_id` INTEGER NOT NULL,
`status` ENUM('Not shipped','Shipped','finish') NOT NULL,
FOREIGN KEY(client_id) REFERENCES client(id) ON DELETE CASCADE ON UPDATE CASCADE,
'''

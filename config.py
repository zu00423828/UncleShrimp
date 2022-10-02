import os
from dotenv import load_dotenv
load_dotenv()


def get_db_setting():
    db_host = os.environ.get('DBHOST')
    db_port = os.environ.get('DBPORT')
    db_user = os.environ.get('DBUSER')
    db_passwd = os.environ.get('DBPASSWD')
    db_name = os.environ.get('DBNAME')
    return db_host, db_port, db_user, db_passwd, db_name


db_host, db_port, db_user, db_passwd, db_name = get_db_setting()


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig
}

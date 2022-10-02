from .common import db
from enum import Enum
from datetime import datetime
from flask_bcrypt import generate_password_hash


class Status(Enum):
    unconfirmed = 'unconfirmed'
    not_shipped = 'not shipped'
    shipped = 'shipped'
    finish = 'finish'


class User(db.Model):
    __table__name = 'user'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text, nullable=False)
    create_datetime = db.Column(db.DateTime, nullable=False)

    def __init__(self, account, password, name, admin, phone, address):
        self.account = account
        self.password = generate_password_hash(password)
        self.name = name
        self.admin = admin
        self.phone = phone
        self.address = address
        self.create_datetime = datetime.now()


class Prodect(db.Model):
    __table__name = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.BLOB, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    depiction = db.Column(db.Text, nullable=False)
    create_datetime = db.Column(db.DateTime, nullable=False)


class Order(db.Model):
    __table__name = 'order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    info = db.Column(db.Text, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    statu = db.Column(db.Enum(Status), nullable=False)
    create_datetime = db.Column(db.DateTime, nullable=False)

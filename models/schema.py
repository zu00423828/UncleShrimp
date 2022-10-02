from email.policy import default
from .common import ma


class UserSchema(ma.Schema):
    id = ma.Int(required=False)
    account = ma.Str(required=True)
    password = ma.Str(required=True)
    admin = ma.Boolean(required=True)
    name = ma.Str(required=True)
    phone = ma.Str(required=True)
    address = ma.Str(required=True)
    create_datetime = ma.DateTime(required=False)


class UserModify(ma.Schema):
    name = ma.Str(required=False)
    phone = ma.Str(required=False)
    address = ma.Str(required=False)


class UserAuth(ma.Schema):
    account = ma.Str(required=True)
    password = ma.Str(required=True)


class AuthSchema(ma.Schema):
    token = ma.Str(required=True)
    expiration_datetime = ma.DateTime(required=True)


class ProductSchema(ma.Schema):
    id = ma.Int(required=False)
    name = ma.String(required=True)
    image_path = ma.String(required=False)
    price = ma.Int(required=True)
    depiction = ma.String(required=True)
    display = ma.Boolean(required=True)
    create_datetime = ma.DateTime(required=False)

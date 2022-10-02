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


class UserAuth(ma.Schema):
    account = ma.Str(required=True)
    password = ma.Str(required=True)


class AuthSchema(ma.Schema):
    token = ma.Str(required=True)
    expiration_datetime = ma.DateTime(required=True)


class ProductSchema(ma.Schema):
    id = ma.Int(required=False)
    name = ma.String(required=True)
    # image = ma.String(required=True)
    price = ma.Int(required=True)
    depiction = ma.Str(required=True)
    display = ma.Boolean(required=True)
    create_datetime = ma.DateTime(required=False)

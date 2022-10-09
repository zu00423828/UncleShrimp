from .common import ma


class UserSchema(ma.Schema):
    id = ma.Int(required=False)
    account = ma.Str(required=True)
    password = ma.Str(required=True)
    admin = ma.Boolean(required=True)
    name = ma.Str(required=True)
    phone = ma.Str(required=True)
    address = ma.Str(required=True)
    create_datetime = ma.Str(required=False)


class UserModify(ma.Schema):
    name = ma.Str(required=False)
    password = ma.Str(required=False)
    phone = ma.Str(required=False)
    address = ma.Str(required=False)


class UserInfo(ma.Schema):
    name = ma.Str(required=True)
    phone = ma.Str(required=True)
    address = ma.Str(required=True)


class UserAuth(ma.Schema):
    account = ma.Str(required=True)
    password = ma.Str(required=True)


class AuthSchema(ma.Schema):
    token = ma.Str(required=True)
    expiration_datetime = ma.Str(required=True)


class ProductSchema(ma.Schema):
    id = ma.Int(required=False)
    name = ma.String(required=True)
    # image_path = ma.String(required=False)
    price = ma.Int(required=True)
    depiction = ma.String(required=True)
    display = ma.Boolean(required=True)
    create_datetime = ma.Str(required=False)
    image_path = ma.Hyperlinks(
        ma.URLFor('productimage', values=dict(id='<id>')))


class ProductModify(ma.Schema):
    name = ma.String(required=False)
    price = ma.Int(required=False)
    depiction = ma.String(required=False)
    display = ma.Boolean(required=False)


class OrderSchema(ma.Schema):
    id = ma.Int(required=False)
    user_id = ma.Int(requied=True)
    info = ma.String(required=True)
    total = ma.Int(required=True)
    status = ma.String(required=True)
    create_datetime = ma.Str(required=False)
    user_info = ma.Nested(UserInfo)


class OrderModify(ma.Schema):
    status = ma.String(required=True)

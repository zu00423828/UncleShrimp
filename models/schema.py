from email.policy import default
from .common import ma
from datetime import datetime


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

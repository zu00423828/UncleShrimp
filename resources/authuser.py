from cgitb import reset
from flask import request
from flask_restful import Resource
from models import db, User
from models.schema import UserAuth, UserSchema
from flask_bcrypt import check_password_hash


class AuthApi(Resource):
    def post(self):
        data = UserAuth().load(request.json)
        result = db.session.query(User).filter_by(
            account=data['account']).first()
        auth_state = check_password_hash(result.password, data['password'])
        return auth_state

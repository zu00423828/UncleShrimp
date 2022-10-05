from datetime import datetime
from flask import request, g
from flask_restful import Resource
from flask_httpauth import HTTPTokenAuth
from models import db, User, Auth
from models.schema import UserAuth, AuthSchema
from flask_bcrypt import check_password_hash
from hashlib import sha256
import os

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    g.user_id = None
    info: Auth = db.session.query(Auth).filter_by(token=token).first()
    if not info:
        return False
    if datetime.now() > info.expiration_datetime:
        return False
    g.user_id = info.user_id
    return True


class AuthApi(Resource):
    def post(self):
        data = UserAuth().load(request.json)
        result = db.session.query(User).filter_by(
            account=data['account']).first()
        auth_state = check_password_hash(result.password, data['password'])
        if not auth_state:
            return {'message': 'login error'}, 400
        auth_info = self.create_token(result)
        return auth_info

    def create_token(self, user_info: User):
        content = user_info.account+str(os.urandom(32))
        token = sha256(content.encode()).hexdigest()
        auth_info = Auth(user_info.id, token)
        db.session.add(auth_info)
        db.session.commit()

        return AuthSchema().dump(auth_info)

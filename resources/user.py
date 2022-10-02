from flask import request
from flask_restful import Resource
from models.schema import UserSchema, UserAuth
from models import db, User


class UsersApi(Resource):
    def post(self):
        userschema = UserSchema()
        result = userschema.load(request.json)
        user = User(**result)
        db.session.add(user)
        db.session.commit()
        return userschema.dump(user)


class UserApi(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

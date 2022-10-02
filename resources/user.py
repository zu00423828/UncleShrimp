from flask import request, g
from flask_restful import Resource
from models.schema import UserSchema
from models import db, User
from .authuser import auth


class UsersApi(Resource):
    def post(self):
        userschema = UserSchema()
        result = userschema.load(request.json)
        user = User(**result)
        db.session.add(user)
        db.session.commit()
        return userschema.dump(user)

    @auth.login_required
    def put(self):
        userschema = UserSchema()
        user: User = User.query.filter_by(id=g.user_id).first()
        user.address = '123xxx'
        db.session.commit()
        return userschema.dump(user)

    @auth.login_required
    def delete(self):
        user = User.query.filter_by(id=g.user_id).first()
        db.session.delete(user)
        db.session.commit()


class UserApi(Resource):

    def put(self):
        pass

    def delete(self):
        pass

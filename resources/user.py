from collections import UserList
from flask import request, g
from flask_restful import Resource
from models.schema import UserSchema, UserModify
from models import db, User
from .authuser import auth


class UsersApi(Resource):
    user_schema = UserSchema()
    user_modify = UserModify()

    def post(self):
        data = self.user_schema.load(request.json)
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return self.user_schema.dump(user)

    @auth.login_required
    def put(self):
        data = self.user_modify.load(request.json)
        User.query.filter_by(id=g.user_id).update(data)
        db.session.commit()
        user = User.query.filter_by(id=g.user_id).first()
        return self.user_schema.dump(user)

    @auth.login_required
    def delete(self):
        user = User.query.filter_by(id=g.user_id).first()
        db.session.delete(user)
        db.session.commit()

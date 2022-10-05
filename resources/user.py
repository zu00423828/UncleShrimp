from flask import request, g, jsonify
from flask_restful import Resource
from models.schema import UserSchema, UserModify
from models import db, User
from .authuser import auth


class UsersApi(Resource):
    user_schema = UserSchema()
    user_modify = UserModify()

    def post(self):
        data = self.user_schema.load(request.json)
        try:
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return jsonify(self.user_schema.dump(user))
        except:
            return {'message': "add user error"}, 400

    @auth.login_required
    def put(self):
        data = self.user_modify.load(request.json)
        if 'password' in data:
            from flask_bcrypt import generate_password_hash
            data['password'] = generate_password_hash(data['password'])
        try:
            User.query.filter_by(id=g.user_id).update(data)
            db.session.commit()
            user = User.query.filter_by(id=g.user_id).first()
            return jsonify(self.user_schema.dump(user))
        except:
            return {'message': "modify user error"}, 400

    @auth.login_required
    def delete(self):
        try:
            user = User.query.filter_by(id=g.user_id).first()
            db.session.delete(user)
            db.session.commit()
        except:
            return {'message': "delete user error"}, 400

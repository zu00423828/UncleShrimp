from flask import g
from flask_restful import Resource, output_json, reqparse, request
from models import Order, db
from models.schema import OrderSchema, OrderModify
from .authuser import auth


class OrdersApi(Resource):
    order_schema = OrderSchema()
    decorators = [auth.login_required]

    def get(self):
        try:

            # parser = reqparse.RequestParser()
            # parser.add_argument("limit", required=False, default=20)
            # parser.add_argument("page", required=False, default=1)
            # args = parser.parse_args()
            args = request.args
            if 'limit' not in args:
                limit = 20
            if 'page' not in args:
                page = 1
            offset = (page-1)*limit
            print(limit, offset)
            count = Order.query.count()
            data = Order.query.offset(offset).limit(limit).all()
            # data = Order.query.all()
            data = self.order_schema.dump(data, many=True)
            return output_json(data=data, code=200, headers={'order-total': count})
        except Exception as e:
            print('happend errors')
            print(e)

    def post(self):
        data = self.order_schema.load(request.json)
        try:
            order = Order(**data, user_id=g.user_id)
            db.session.add(order)
            db.session.commit()
            return output_json(self.order_schema.dump(order), 200)
        except:
            return {'message': "add oder error"}, 400


class OrderApi(Resource):
    decorators = [auth.login_required]

    def put(self, id):
        try:
            order_modify = OrderModify()
            data = order_modify.load(request.json)
            Order.query.filter_by(id=id).update(data)
            db.session.commit()
            order = Order.query.filter_by(id=id).first()
            return output_json(OrderSchema().dump(order), code=200)
        except Exception as e:
            print(e)
            return {'message': "modify oder error"}, 400

    def delete(self, id):
        try:
            order = Order.query.filter_by(user_id=g.user_id, id=id).first()
            db.session.delete(order)
            db.session.commit()
        except:
            return {'message': "delete user error"}, 400

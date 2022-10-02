from io import BytesIO
from flask import request
from flask_restful import Resource
from .authuser import auth
from models import db, Product
from models.schema import ProductSchema
from io import BytesIO


class ProductsApi(Resource):
    def get(self):
        pass

    def post(self):
        productschema = ProductSchema()
        data = request.form
        data = productschema.load(request.form)
        image = request.files['image'].read()
        product = Product(**data, image=image)
        # product = Product(name=data['name'], image=BytesIO(), price=data['price'],
        #                   depiction=data['depiction'], display=data['display'])
        db.session.add(product)
        db.session.commit()
        return {'test': 'test'}
        # return productschema.dump(product)


class ProductApi(Resource):
    decorators = [auth.login_required]

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

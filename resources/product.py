from flask import request, send_file, jsonify, make_response
from flask_restful import Resource, reqparse
from .authuser import auth
from models import db, Product
from models.schema import ProductSchema, ProductModify
from io import BytesIO


class ProductsApi(Resource):
    product_schema = ProductSchema()

    def get(self):
        decorators = [auth.login_required]
        parser = reqparse.RequestParser()
        parser.add_argument("limit", required=False, default=20)
        parser.add_argument("page", required=False, default=1)
        args = parser.parse_args()
        limit = args['limit']
        offset = (args['page']-1)*limit
        products: Product = Product.query.offset(offset).limit(limit).all()
        count = Product.query.count()
        for product in products:
            product.image_path = f'/api/product-image/{product.id}'
        resp = make_response(
            jsonify(self.product_schema.dump(products, many=True)), 200)
        resp.headers['product-total'] = count
        return resp

    def post(self):
        decorators = [auth.login_required]
        try:
            data = request.form
            data = self.product_schema.load(request.form)
            image = request.files['image'].read()
            product = Product(**data, image=image)
            db.session.add(product)
            db.session.commit()
            product.image_path = f'/api/product-image/{product.id}'
            return jsonify(self.product_schema.dump(product))
        except:
            return {'message': "add prouct error"}, 400


class ProductImage(Resource):
    def get(self, id):
        product: Product = Product.query.filter_by(id=id).first()
        image_content = BytesIO(product.image)
        return send_file(image_content, mimetype="image/png")


class ProductApi(Resource):
    decorators = [auth.login_required]
    product_schema = ProductSchema()
    product_modify = ProductModify()

    def put(self, id):
        data = self.product_modify.load(request.form)
        if request.files:
            data['image'] = request.files['image'].read()
        try:
            Product.query.filter_by(id=id).update(data)
            db.session.commit()
            product = Product.query.filter_by(id=id).first()
            product.image_path = f'/api/product-image/{product.id}'
            return self.product_schema.dump(product)
        except:
            return {'message': "modify prouct error"}, 400

    def delete(self, id):
        try:
            product = Product.query.filter_by(id=id).first()
            db.session.delete(product)
            db.session.commit()
            return {'message': 'delete sussess'}
        except:
            return {'message': "delete prouct error"}, 400

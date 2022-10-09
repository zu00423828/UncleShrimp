from flask import request, send_file
from flask_restful import Resource, reqparse, output_json
from .authuser import auth
from models import db, Product
from models.schema import ProductSchema, ProductModify
from io import BytesIO


class ProductsApi(Resource):
    product_schema = ProductSchema()
    decorators = [auth.login_required]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("limit", required=False, default=20)
        parser.add_argument("page", required=False, default=1)
        args = parser.parse_args()
        limit = args['limit']
        offset = (args['page']-1)*limit
        products: Product = Product.query.offset(offset).limit(limit).all()
        count = Product.query.count()
        resp = output_json(data=self.product_schema.dump(
            products, many=True), code=200, headers={'product-total': count})
        return resp

    def post(self):
        try:
            data = request.form
            print('hello')
            data = self.product_schema.load(request.form)
            print('hello2')
            image = request.files['image'].read()
            print('hello3')
            product = Product(**data, image=image)
            print('hello4')
            db.session.add(product)
            db.session.commit()
            return output_json(data=self.product_schema.dump(product), code=200)
        except Exception as e:
            print(e)
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

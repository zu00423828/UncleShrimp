from flask import request, send_file, jsonify
from flask_restful import Resource
from .authuser import auth
from models import db, Product
from models.schema import ProductSchema
from io import BytesIO


class ProductsApi(Resource):
    product_schema = ProductSchema()

    def get(self):
        products: Product = Product.query.all()
        for product in products:
            product.image_path = f'/product/{product.id}'
        return jsonify(self.product_schema.dump(products, many=True))

    def post(self):
        data = request.form
        data = self.product_schema.load(request.form)
        image = request.files['image'].read()
        product = Product(**data, image=image)
        # product = Product(name=data['name'], image=BytesIO(), price=data['price'],
        #                   depiction=data['depiction'], display=data['display'])
        db.session.add(product)
        db.session.commit()
        return {'test': 'test'}
        # return productschema.dump(product)


class ProductImage(Resource):
    def get(self, id):
        product: Product = Product.query.filter_by(id=id).first()
        image_content = BytesIO(product.image)
        return send_file(image_content, mimetype="image/png")


class ProductApi(Resource):
    decorators = [auth.login_required]
    product_schema = ProductSchema()

    def put(self, id):
        data = self.product_schema.load(request.form)
        Product.query.filter_by(id=id).update(data)
        db.session.commit()
        product = Product.query.filter_by(id=id).first()
        return self.product_schema.dump(product)

    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()

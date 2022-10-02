from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import config
from resources import *
from models import db, ma
from resources.authuser import AuthApi
from resources.product import ProductImage

app = Flask(__name__)
app.config.from_object(config['development'])
CORS(app)
api = Api(app)
api.add_resource(AuthApi, '/api/auth')
api.add_resource(UsersApi, '/api/users')
api.add_resource(ProductsApi, '/api//products')
api.add_resource(ProductApi, '/api/product/<int:id>')
api.add_resource(ProductImage, '/product/<int:id>')
api.add_resource(OrdersApi, '/api/orders')
api.add_resource(OrderApi, '/api/order/<int:id>')


db.init_app(app)
with app.app_context():
    db.create_all()
ma.init_app(app)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)

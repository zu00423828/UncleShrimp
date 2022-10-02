from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from config import config
from resources import *
from models import db, ma
from resources.authuser import AuthApi

app = Flask(__name__)
app.config.from_object(config['development'])
CORS(app)

api = Api(app)
api.add_resource(AuthApi, '/auth')
api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/user/<int:id>')
api.add_resource(ProductsApi, '/products')
api.add_resource(ProductApi, '/product/<int:id>')
api.add_resource(OrdersApi, '/orders')
api.add_resource(OrderApi, '/order/<int:id>')


class TestApi(Resource):
    def get(self):
        return 123


api.add_resource(TestApi, '/test')

db.init_app(app)
with app.app_context():
    db.create_all()
ma.init_app(app)


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)

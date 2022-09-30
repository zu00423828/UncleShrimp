from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources import *
from config import config
from models import db, ma
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.config.from_object(config['development'])
CORS(app)
api = Api()
db.init_app(app)
with app.app_context():
    print('init')
#     db.create_all()
ma.init_app(app)
api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/user/<int:id>')
api.add_resource(ProductsApi, '/products')
api.add_resource(ProductApi, '/product/<int:id>')
api.add_resource(OrdersApi, '/orders')
api.add_resource(OrderApi, '/order/<int:id>')


@app.route('/')
def root():
    return "welcome  UncleShrimp website"


if __name__ == '__main__':
    app.run(debug=True)

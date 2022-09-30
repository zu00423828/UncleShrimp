from flask import Flask
from flask_restful import Api
from resources import *
app = Flask(__name__)
api = Api()
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

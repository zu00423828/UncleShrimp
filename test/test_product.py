import json
import requests

api_root = 'http://localhost:5000'
productsApi = f'{api_root}/api/products'
productApi = f'{api_root}/api/product'
authApi = f'{api_root}/api/auth'


def login_user():
    login_data = {'account': 'zu00423828', 'password': 'zu7957232'}
    res = requests.post(authApi, json=login_data)
    return res.json()


def create_product(login_info):
    token = login_info['token']
    headers = {'Authorization': f'Bearer {token}'}
    product_data = {'name': 'product 1', 'price': 100,
                    'depiction': 'product xxxxx', 'display': True}
    file = {'image': open('mock_data/1.webp', 'rb').read()}
    res = requests.post(productsApi, headers=headers,
                        data=product_data, files=file)
    print(res.json())


def get_products(login_info):
    token = login_info['token']
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.get(productsApi, headers=headers)
    print(res.headers, res.json(), len(res.json()))


def modify_product(login_info):
    token = login_info['token']
    headers = {'Authorization': f'Bearer {token}'}
    product_data = {'price': 150,
                    'depiction': 'product xxxxx', 'display': True}
    file = {'image': open('mock_data/1.webp', 'rb').read()}
    # file = {'image': open('mock_data/2.jpg', 'rb').read()}
    res = requests.put(productApi+'/1', headers=headers,
                       data=product_data, files=file)
    print(res.json())


def delete_product(login_info):
    token = login_info['token']
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.delete(productApi+'/1', headers=headers)
    print(res.json())


if __name__ == "__main__":
    login_info = login_user()
    create_product(login_info)
    # get_products(login_info)
    # modify_product(login_info)
    # delete_product(login_info)

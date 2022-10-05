import requests

api_root = 'http://localhost:5000'
usersApi = f'{api_root}/api/users'
authApi = f'{api_root}/api/auth'


def create_user():
    user_data = {'account': 'zu00423828', 'password': 'zu7957232',
                 'admin': True, 'name': '鍾奉原', 'phone': '0983192826', 'address': 'xxx-xxx-xxx-xxx'}
    res = requests.post(usersApi, json=user_data)
    print(res.json())


def login_user(login_data):

    res = requests.post(authApi, json=login_data)
    print(res.json())
    return res.json()


def modify_user(login_info):
    token = login_info['token']
    print(token)
    modify_data = {'phone': '1234567890',
                   'address': '123xxxx23213', 'password': '123'}
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.put(usersApi, headers=headers, json=modify_data)
    print(res.json())


if __name__ == "__main__":
    try:
        create_user()
    except:
        pass
    login_data = {'account': 'zu00423828', 'password': 'zu7957232'}
    login_info = login_user(login_data)
    modify_user(login_info)
    login_data = {'account': 'zu00423828', 'password': '123'}
    login_info = login_user(login_data)

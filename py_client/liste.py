import requests
from getpass import getpass

username = input("What is your name ")
password = getpass("What is your password ")
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
auth_res = requests.post(auth_endpoint, json={'username' : username, 'password': password})
print(auth_res.json())

if auth_res.status_code==200:
    token = auth_res.json()['token']
    headers={
        'Authorization' : f'Bearer {token}'
    }
    endpoint = "http://127.0.0.1:8000/api/products/"
    res = requests.get(endpoint, headers=headers)
    print(res.json())

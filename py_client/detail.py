import requests

endpoint = "http://127.0.0.1:8000/api/products/8"

res = requests.get(endpoint)
# print(res.headers)
print(res.json())

# print(res.status_code)
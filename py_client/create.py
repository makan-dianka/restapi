import requests

endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title" : "this field is done",
    "price" : 32.99
}
res = requests.post(endpoint, json=data)
# print(res.headers)
print(res.json())

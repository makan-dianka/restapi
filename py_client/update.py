import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update"
data = {
    'title' : "Hello world",
    'price' : 00.00,
}
res = requests.put(endpoint, json=data)
# print(res.headers)
print(res.json())

# print(res.status_code)
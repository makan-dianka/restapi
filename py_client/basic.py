import requests

endpoint = "http://127.0.0.1:8000/api/"

res = requests.post(endpoint, json={"title" : "abc123", "content" : "Hello Toto", "price":123})
# print(res.headers)
print(res.json())

# print(res.status_code)
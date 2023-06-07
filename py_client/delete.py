import requests

try:
    product_id = int(input("What is the product id ? "))
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete"

    res = requests.delete(endpoint)
    # print(res.headers)
    print(res.status_code, res.status_code==204)

    # print(res.status_code)
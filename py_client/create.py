import requests

headers = {"Authorization": "Bearer 50457de3d05ec503f4c525f82149f000a2b871ce"}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "This field is Done", "price": 32.99}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())

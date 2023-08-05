import requests
url = 'http://127.0.0.1:8000/api/token/'

data = {'username': 'etozhedin', 'password': '1234'}
response = requests.post(url, json=data)
print(response.json())

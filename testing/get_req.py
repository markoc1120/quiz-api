import requests

endpoint = "http://localhost:8001/api/"

data = requests.get(endpoint)

print(data.json())


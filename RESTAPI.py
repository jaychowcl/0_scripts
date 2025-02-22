import requests
import json

url = "https://restapi.com/api/x"

headers = {
    "Auth" : "TOKEN"
}

response = requests.get(url, headers = headers)

print(response.status_code)
print(response.json())

payload = {
    "username" : "jay",
    "address" : {
        "street" : "x",
        "country" : "y"
    }
}

response = requests.post((url, data = json.dumps(payload), headers = headers))

print(response.status_code)
print(response.json())
print(response.text())
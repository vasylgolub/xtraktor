import requests

BASE = "http://localhost:5000/"

filepath = "/Users/vasylgolub/Desktop/pdfs/2021/September 01, 2021.pdf"
headers = {"Content-Type": "application/json; charset=utf-8"}

# with open(filepath, 'rb') as f:
#     response = requests.put(BASE + "upload", data={'d': "some data"}, files={'file': f})

# response = requests.put(BASE + "upload", data={'data': 'dadada'})

response = requests.get(BASE + "get")

print("Status Code", response.status_code)
print("JSON Response ", response.json())
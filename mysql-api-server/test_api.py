import requests

response = requests.post(
    "http://127.0.0.1:5000/query",
    json={"query": "SELECT * FROM Answer LIMIT 1"}
)

print(response.json())

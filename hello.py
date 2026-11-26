import requests

response = requests.get("https://api.github.com")
print("Code:", response.status_code)
print("Привет из ветки!")

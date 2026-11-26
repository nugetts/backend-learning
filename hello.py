import requests

response = requests.get("https://api.github.com")
print("Статус:", response.status_code)
print("Привет из ветки!")

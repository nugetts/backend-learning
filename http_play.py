import requests

r = requests.get("https://api.github.com/users/nugetts")
print(r.status_code)
print(r.headers['content-type'])
data = r.json()
print(data["login"])
print(data["public_repos"])

r2 = requests.get("https://api.github.com/users/no-such-user-zzz-12345")
print(r2.status_code)
print(r2.json())
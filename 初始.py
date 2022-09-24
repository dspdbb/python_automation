import requests

url = 'https://v0.yiketianqi.com/free/day'
data = {"appid": "56485388", "appsecret": "hLIg5d0L", "city": "台州"}
res = requests.get(url,data)
print(res.json())

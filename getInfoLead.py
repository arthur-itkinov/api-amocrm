import requests

with open('access_token.txt', 'r') as access:
    access_token = access.read()



header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/hal+json",
    "Content-Type": "application/json"
}
params = {
    "id": '8857618'
}
id = '29155773'

url = f'https://fortunaperm.amocrm.ru/api/v4/leads/{id}'
res = requests.get(url, headers=header)
print(res.status_code)
print(res.json())

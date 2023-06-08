import requests


client_id = "xxx" # скопировать из настроек интеграции амосрм
client_secret = "xxx" # скопировать из настроек интеграции амосрм
subdomain = "xxx" # скопировать из настроек интеграции амосрм
redirect_url = "xxx" # скопировать из настроек интеграции амосрм
with open('refresh_token.txt', 'r') as access: # refresh_token.txt будет автоматически создан при первой регистрации
    refresh_token = access.read() 


def recovery_token():
    url = f'https://{subdomain}.amocrm.ru/oauth2/access_token'
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "redirect_uri": subdomain
    }
    header = {
        "Content-Type": "application/json",
    }

    res = requests.post(url, headers=header, json=params)
    print(res.status_code)
    print(res.json())
    token = res.json()
    # перезаписываем новый access_token и refresh_token
    with open("access_token.txt", "w") as file:
        file.write(token['access_token'])
    with open("refresh_token.txt", "w") as file:
        file.write(token['access_token'])

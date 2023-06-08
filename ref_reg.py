import requests


client_id = "f5c13476-5c79-4c25-9eac-7a0b8c5a7a18"
client_secret = "IGQ8TsVIZWntM0reoCJkVuYWYM6UEhnIeTl4cBUlyCduD8UzWZemsaEtp5surpAY"
subdomain = "fortunaperm"
redirect_url = "https://aktivkredit.ru/"
with open('refresh_token.txt', 'r') as access:
    refresh_token = access.read()


def recovery_token():
    url = f'https://fortunaperm.amocrm.ru/oauth2/access_token'
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
    with open("access_token.txt", "w") as file:
        file.write(token['access_token'])
    with open("refresh_token.txt", "w") as file:
        file.write(token['access_token'])

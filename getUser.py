import requests
from getEmtity import emtity


def getUser(idLead):
    idUser = emtity(idLead)
    with open('access_token.txt', 'r') as access:
        access_token = access.read()

    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/hal+json",
        "Content-Type": "application/json"
    }

    url = f'https://fortunaperm.amocrm.ru/api/v4/contacts/{idUser}'
    res = requests.get(url, headers=header)
    result = res.json()

    return result

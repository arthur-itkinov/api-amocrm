import requests


def emtity(idLead):
    subdomain = "xxx" # скопировать из настроек интеграции или из адресной строки
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

    url = f'https://{subdomain}.amocrm.ru/api/v4/leads/{idLead}/links'
    res = requests.get(url, headers=header)
    result = res.json()
    userId = result['_embedded']['links'][0]['to_entity_id']
    return userId

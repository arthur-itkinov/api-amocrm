import os
import shutil
from amocrm.v2 import tokens, Lead, Pipeline, Status, Company, Contact
import requests
import datetime
from createExcel import create_excel_file
from getLeadsExcel import add_leads_in_excel
from mail import send_email
from ref_reg import recovery_token

now = datetime.datetime.now()
delta = datetime.timedelta(days=1)
dateback = now - delta
dayback = dateback.strftime("%d")
monthback = dateback.strftime("%m")
yearback = dateback.strftime("%Y")
start_day = f'{yearback}-{monthback}-{dayback} 00:00:00'
end_day = f'{yearback}-{monthback}-{dayback} 23:59:59'


start_day_utc = datetime.datetime.strptime(
    start_day, '%Y-%m-%d %H:%M:%S').timestamp()
end_day_utc = datetime.datetime.strptime(
    end_day, '%Y-%m-%d %H:%M:%S').timestamp()

with open('access_token.txt', 'r') as access:
    access_token = access.read()

header = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/hal+json",
    "Content-Type": "application/json"
}
params = {

    "filter[pipe][721543][]": "19569811",
    "filter[created_at][from]": f"{start_day_utc}",
    "filter[created_at][to]": f"{end_day_utc}",
    "useFilter": 'y'
}


def cron_get_leads_post_email():
    url = f'https://fortunaperm.amocrm.ru/api/v4/leads'
    res = requests.get(url, headers=header, params=params)
    if res.status_code == 200:
        result = res.json()
        if result:
            create_excel_file()
            for lead in result['_embedded']['leads']:
                # print(lead['name'], lead)
                add_leads_in_excel(lead)
            send_email('itkinov-a@mail.ru')
            send_email('itkinov-a@mail.ru')
            path = f'./Отчет за {dayback}-{monthback}-{yearback}.xlsx'
            os.remove(path)

    else:
        recovery_token()
        cron_get_leads_post_email()


cron_get_leads_post_email()

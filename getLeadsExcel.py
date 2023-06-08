import datetime
import openpyxl
from getUser import getUser
from searchPartner import search_partner

now = datetime.datetime.now()
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
dateback = today - delta
dayback = dateback.strftime("%d")
monthback = dateback.strftime("%m")
yearback = dateback.strftime("%Y")


def add_leads_in_excel(lead):
    userInfo = getUser(lead['id'])
    fn = f'Отчет за {dayback}-{monthback}-{yearback}.xlsx'
    wb = openpyxl.load_workbook(fn)
    ws = wb['Sheet']
    print(lead)
    # for lead in leads:
    #     leadId = lead['id']
    ws.append([lead['id'],
               lead['name'],
               userInfo['name'],
               lead['price'],
               userInfo['custom_fields_values'][1]['values'][0]['value'],
               search_partner(lead['custom_fields_values']),
               ])
    wb.save(fn)
    wb.close()

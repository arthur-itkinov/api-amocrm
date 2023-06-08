import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
import datetime

now = datetime.datetime.now()
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
dateback = today - delta
dayback = dateback.strftime("%d")
monthback = dateback.strftime("%m")
yearback = dateback.strftime("%Y")


alignment = Alignment(horizontal='general',
                      vertical='bottom',
                      text_rotation=0,
                      wrap_text=False,
                      shrink_to_fit=False,
                      indent=0)


def create_excel_file():
    book = openpyxl.Workbook()
    sheet = book.active

    a1 = sheet['A1']
    b1 = sheet['B1']
    c1 = sheet['C1']
    d1 = sheet['D1']
    e1 = sheet['E1']
    f1 = sheet['F1']
    a1.alignment = Alignment(horizontal='center', vertical='center')
    b1.alignment = Alignment(horizontal='center', vertical='center')
    c1.alignment = Alignment(horizontal='center', vertical='center')
    d1.alignment = Alignment(horizontal='center', vertical='center')
    e1.alignment = Alignment(horizontal='center', vertical='center')
    f1.alignment = Alignment(horizontal='center', vertical='center')
    a1.font = Font(size=16, bold=True)
    b1.font = Font(size=16, bold=True)
    c1.font = Font(size=16, bold=True)
    d1.font = Font(size=16, bold=True)
    e1.font = Font(size=16, bold=True)
    f1.font = Font(size=16, bold=True)
    sheet.column_dimensions['A'].width = 20
    sheet.column_dimensions['B'].width = 40
    sheet.column_dimensions['C'].width = 40
    sheet.column_dimensions['D'].width = 20
    sheet.column_dimensions['E'].width = 40
    sheet.column_dimensions['F'].width = 40

    sheet['A1'] = 'ID сделки'
    sheet['B1'] = 'Название'
    sheet['C1'] = 'ФИО'
    sheet['D1'] = 'Сумма'
    sheet['E1'] = 'Почта или ссылка на анкету'
    sheet['F1'] = 'Название партнера'
    book.save(f'Отчет за {dayback}-{monthback}-{yearback}.xlsx')
    book.close()

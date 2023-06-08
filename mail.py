import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mimetypes
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
import datetime

now = datetime.datetime.now()
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
dateback = today - delta
dayback = dateback.strftime("%d")
monthback = dateback.strftime("%m")
yearback = dateback.strftime("%Y")


def send_email(toEmail):
    sender = 'itkinov6@gmail.com'
    passwd = "xvisibffirlmkuni"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, passwd)
        msg = MIMEText('Во вложении файл со сделками по которм нужны чеки')
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = toEmail
        msg['Subject'] = 'Отчет по сделкам с чеками'

        msg.attach(MIMEText("Отчет по сделкам с чеками"))

        with open(f'Отчет за {dayback}-{monthback}-{yearback}.xlsx', 'rb') as f:
            file = MIMEApplication(f.read())
        file.add_header('content-disposition',
                        'attachment', filename='report.xlsx')
        msg.attach(file)

        server.sendmail(sender, toEmail, msg.as_string())

        return "the message was sent successfully"
    except Exception as _ex:
        return f"{_ex}\n check your login or password"

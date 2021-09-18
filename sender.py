import smtplib
import os
from email.mime.text import MIMEText

users = ['jintaxi97@gmail.com', 'evn06@mail.ru', 'veduser@mail.ru']

password = os.getenv("EMAIL_PASSWD")
sender = 'jintaxi.mailing@gmail.com'
server = smtplib.SMTP("smtp.gmail.com")

server.starttls()


# Оповещение
def send_mail(mail):

    mail = MIMEText(f"{mail}")
    mail['Subject'] = "Отслеживание рыбы"  

    try:
        server.login(sender, password)
        for user in users:
            server.sendmail(sender, user, f"{mail}")
    except Exception as _ex:
        print (f"[ERROR] {_ex}")

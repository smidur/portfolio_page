import smtplib, ssl
from os import getenv


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = getenv("PROJECT_USER")
    password = getenv("PROJECT_PASSWD")

    receiver = getenv("PROJECT_USER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

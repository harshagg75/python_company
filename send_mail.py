import smtplib,ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "email.com"
    password = "password"

    receiver = "email.com"
    context1 = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context1) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

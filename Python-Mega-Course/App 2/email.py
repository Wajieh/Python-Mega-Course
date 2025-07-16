import smtplib, ssl
def send_email():
    host = "smtp.gmail.com"
    port = 465

    username = "sum@gmail.com"
    password = "sumkey"

    receiver = "anotheremail@gmail.com"
    context = ssl.create_default_context()
    message = ""

    with smtplib.SMTP_SSL(host,port,context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
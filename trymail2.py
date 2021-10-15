import smtplib

gmail_user = input(str("username: "))
gmail_app_password = input(str("password: "))

with open('finalprojecttrial.txt', 'r') as content:
    recipient = content.read().replace('\n', ',')

sent_from = gmail_user
sent_to = recipient
sent_subject = input(str("Email subject: "))
sent_body = input(str("type your message here: "))

email_text = """\
from: %s
to: %s
subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)


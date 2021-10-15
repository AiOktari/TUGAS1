#import module Yagmail
import yagmail

#definisi variabel (subject, isi, dan attachment file pada email)
subject = 'Final Project Basic Python'
content = 'Trial 2'
berkas = r'D:\Pictures\SHEOAK PORTFOLIO 1.jpg'

#input pengirim email
user_email = str(input('Username : '))
user_password = str(input('Password : '))

#ambil email tujuan dari list
with open("finalprojecttrial.txt", "r") as filex:
    list_email = filex.read().splitlines()

try:
    #initializing the server connection
    yag = yagmail.SMTP(user=user_email, password=user_password)
    #sending the email
    yag.send(to= list_email,  subject=subject, contents=content, attachments= berkas)
    print("Email sent successfully")
except:
    print("Error, email was not sent")
import smtplib

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

user = input("Username: ")
pawd = input("Password: ")
server.login(user, pawd)

to = input("to: ")
cc = input("CC: ")
bcc = input("BCC: ")
sub = input("Subject: ")
mes = input("Message: ")

header = f"To: {to}\n"
header += f"CC: {cc}\n"
header += f"BCC: {bcc}\n"
header += f"Subject: {sub}\n\n"

mes = header + f"{mes}"

to = [f"{to}"]
if cc:
    to.append(f"{cc}")
    
if bcc:
    to.append(f"{bcc}")
    

server.sendmail(user, to, mes)
server.quit()
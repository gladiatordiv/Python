import smtplib
sender_email="divyabwr30702@gmail.com"
rec_email="chauhandivya3001@gmail.com"
password=input(str("Please enter your password: "))
message="Hey, this was sent using python"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print("Login Success")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent",rec_email)
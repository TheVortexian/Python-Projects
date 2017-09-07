import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#login
username = str(input("Username / Email: "))
password = str(input("Password: "))
server.login(username, password)
msg = "Test!"
server.sendmail("treesofgold7@gmail.com", "connorleu@icloud.com", msg)
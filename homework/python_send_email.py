import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("dejesushonorio03@gmail.com", "ony199103")
my_messages = ("Hello!")
server.sendmail("dejesusony@gmail.com", "onorio@catalpa.io", my_messages)

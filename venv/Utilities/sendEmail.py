import smtplib

# server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#
# server.login("kamblemahendra77@gmail.com","Mahen@76")
# server.sendmail("mahendra@tmoksha.com","mahendra@techbodhi.com","Testing MAil Api")
# server.quit()

fromaddr = 'kamblemahendra77@gmail.com'
toaddrs  = 'mahendra@techbodhi.com'
msg = 'Python MAIL API email Test'

username = 'kamblemahendra77@gmail.com'
password = 'Mahen@76'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
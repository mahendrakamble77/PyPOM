# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "kamblemahendra77@gmail.com"
toaddr = "mahendra@techbodhi.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail
body = "Body_of_the_mail"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "test.log"
attachment = open("test.log", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "Mahen@76")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
#
#
# def send_mail (sender_address, receiver_address, subject, mail_content, attach_file_name,
#                ) :
#     sender_pass = 'Selenium@234'
#
#     # Setup the MIME
#     message = MIMEMultipart ()
#     message['From'] = sender_address
#     message['To'] = receiver_address
#     message['Subject'] = subject
#
#     # The subject line
#     # The body and the attachments for the mail
#     message.attach ( MIMEText ( mail_content, 'plain' ) )
#     attach_file = open ( attach_file_name, 'rb' )  # Open the file as binary mode
#     payload = MIMEBase ( 'application', 'octate-stream' )
#     payload.set_payload ( (attach_file).read () )
#     encoders.encode_base64 ( payload )  # encode the attachment
#     # add payload header with filename
#     payload.add_header ( 'Content-Disposition', 'attachment', filename = attach_file_name )
#     message.attach ( payload )
#
#     # Create SMTP session for sending the mail
#     session = smtplib.SMTP_SSL ( "smtp.gmail.com", 465 )
#     session.login ( sender_address, sender_pass )  # login with mail_id and password
#     text = message.as_string ()
#     session.sendmail ( sender_address, receiver_address, text )
#     session.quit ()
#     print ( 'Mail Sent' )

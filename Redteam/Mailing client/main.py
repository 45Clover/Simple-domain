import smtplib
#Simple Mail Transfer Protocol (SMTP)
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#Multipurpose Internet Mail Extensions

server = smtplib.SMTP('smtp.gmail', 25)

server.ehlo()
#starting function

# for encrpted txt password 

with open('password', 'r') as f:
    password = f.read()

server.login('Ye2024@gg.com', password)

msg = MIMEMultipart()
msg['From'] = 'Rome'
msg['To'] = 'random@me.com'
msg['Subject'] = 'practise'


with open('meassage.txt', 'r') as f:
    message = f.read()


msg.attach(MIMEText(message, 'plain'))

filename = 'Riela-downs.png'
#yeah i wrote that
attachment = open(filename, 'rb')
# rb = reading byte mode

p = MIMEBase('application', 'octect-stream')
p.set_payload(attachment.read())
#An "octet-stream" is a MIME (Multipurpose Internet Mail Extensions) type used to denote a binary file format. The term "octet" refers to an 8-bit byte, and "stream" refers to a sequence of bytes. This MIME type is used to indicate that the content is a binary data stream and should be treated as such by email clients or web browsers.

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('Ye2024@gg.com', 'random@me.com', text)


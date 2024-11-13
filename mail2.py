import smtplib

from email.mime.multipart import MIMEMultipart  #multi purpose internet mail extension(MIME)
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



from email import encoders
fromaddr="shahinshas809@gmail.com"
toaddr="shazzshahinsha9@gmail.com"

#instance of MIMEMultipart

msg=MIMEMultipart()
#storing the sender email address
msg['From']='shahinshas809@gmail.com'
#storing the reciever email address
msg['To']='shazzshahinsha9@gmail.com'
#storing the subject
msg['subject']="python"
#string to store the body of the mail
# body="welcome to the world of python 😒"

body="""
<html>
<head></head>
<body>
<h1><i>welcome to the world of python</i?</h1>
</body>"""
#attach the body with the msg instance
# msg.attach(MIMEText(body,'plain'))
msg.attach(MIMEText(body,'html')) #convert to plain text and attach

#attach(part)
#part is like MIMEText for plain text
#plain-content type indicate that the content of the email is plain text

filename="list.py"
attachment=open(filename,"rb")
# instance of MIMEBase and named as p
#application::general application
#octet-stream:: attachment is an arbitarybinary file

p=MIMEBase('application','octet-stream')

#to change the pay___load into encoded form
#for example,if you attach a file thats a custom binary format or a generic binary
#file(eg. a .bin or .dat file),you might use 'application/octet-stream' as the
#content type to avoid any automatic processing or rendering by the recipient's email client.it tells the email client to treat the attachment as binary
#data and not try to open it or display it as a specific file type

p.set_payload((attachment).read())

# set_payload():This is a method used to set the content (payload) of the MIMNEBase
#object.in this case,you are setting the payload with the content of a file

#encode into base64

encoders.encode_base64(p)


p.add_header('Content-Disposition',"attachment;filename=%s"% filename)

#attach the instance 'p' to instance 'msg'
msg.attach(p)
#creates SMTP session

s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#authentication


s.login(fromaddr,"vmly zava royb sorc")
#convert the multipart msg into a string
text=msg.as_string()

s.sendmail(fromaddr,toaddr,text)
#terminating the session
s.quit()

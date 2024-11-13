import smtplib #simple mail transfer protocol

s=smtplib.SMTP("smtp.gmail.com",587)

s.starttls()

s.login('shahinshas809@gmail.com',"vmly zava royb sorc")

msg="hello how are you"

s.sendmail("shahinshas809@gmail.com","shazzshahinsha9@gmail.com",msg)

s.quit()
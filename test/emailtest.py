from smtplib import *


def send_email():
    text = "test"
    sender = 'zsdc0306@test.org'
    receivers = ["zhuoqin0@gmail.com","zsdc0306@gmail.com"]
    try:
        smtpObj = SMTP('localhost')
        smtpObj.sendmail(sender, receivers, text)
        print "Successfully sent email"
    except SMTPException as e:
        print "Error: unable to send email"

send_email()

from smtplib import *
import log_util

class email_util(object):
    def __init__(self, max_try=5):
        self.logger = log_util.Logger("logger").get_logger()
        self.admin_email = "zsdc0306@gmail.com"
        self.pick_up_msg = "Iphone 7 is available, Check Now"
        self.error_msg = "Error in getting data, Check"
        self.max_try = max_try
        self.smtpObj = SMTP('localhost')

    def send_email(self, msgtype):
        cur_try = 0
        if msgtype == MSG_ERROR:
            text = "Error in getting data, Check"
        elif msgtype == MSG_PICK:
            text = "Iphone 7 is available, Check Now"
        sender = 'zsdc0306@test.org'
        receivers = ['zsdc0306@gmail.com']
        while cur_try < self.max_try:
            try:
                cur_try += 1
                smtpObj = SMTP('localhost')
                smtpObj.sendmail(sender, receivers, text)
                self.logger.info("Successfully sent email")
            except SMTPException as e:
                error_msg = "Time: %s, ERROR: %s" % (time.strftime('%m-%d,%H:%M:%S',time.localtime(time.time())), e.message)
                self.logger.info(error_msg)
                self.logger.info("Error: unable to send email")
                if cur_try == MAX_TRY:
                    raise e

    def send(self, sender, receivers, text):
        try:
            self.smtpObj.sendmail(sender, receivers, text)
            self.logger.info("Successfully sent email")
        except SMTPException as e:
            self.logger.error("Email send error")
            self.logger.error(e.message)
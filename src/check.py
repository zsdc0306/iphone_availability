import requests
import time
from smtplib import *
import logging

wait_time = 15
MSG_ERROR = 0
MSG_PICK = 1
MAX_TRY = 5

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,
                    format = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s",
 )

model_list={
    "jet":"MN4D2LL%2FA",
    "rose": "MN4C2LL%2FA"
}

users={
    "samuel":{
        "email":"zhuoqin0@gmail.com",
        "model":"jet"
    },
    "zsd":{
        "email":"zsdc0306@gmail.com",
        "model":"rose"
    }
}

def set_url(model):
    model_code = model_list[model]
    url = "http://www.apple.com/shop/retail/pickup-message?parts.0="+model_code+ "&searchNearby=false&cppart=UNLOCKED%2FUS&store=R102"
    return url


def get_pickdate(model):
    url = set_url(model)
    response = requests.get(url)
    if response.status_code != 200:
        logging.error("connection ERROR")
        raise requests.ConnectionError
    else:
        response = response.json()
    stores = response["body"]["stores"]
    city, state = stores[0]["city"], stores[0]["state"]
    pickdate = response["body"]["stores"][0]["partsAvailability"][model_list[model]]["pickupSearchQuote"]
    logging.info("%s, %s, %s", city, state, pickdate)
    return pickdate


def send_email(msgtype, receiver_addr):
    cur_try = 0
    text = ""
    if msgtype == MSG_ERROR:
        text = "Error in getting data, Check"
    elif msgtype == MSG_PICK:
        text = "Iphone 7 is available, Check Now"
    sender = 'zsdc0306@test.org'
    receivers = [receiver_addr]
    while cur_try < MAX_TRY:
        try:
            cur_try += 1
            smtpObj = SMTP('localhost')
            smtpObj.sendmail(sender, receivers, text)
            logging.info("Successfully sent email")
            break
        except SMTPException as e:
            error_msg = "ERROR: %s" % e.message
            logging.info(error_msg)
            logging.info("Error: unable to send email")
            if cur_try == MAX_TRY:
                raise e

def main():
    if len(users) == 0:
        return
    for user in users:
        model = users[user]["model"]
        print model
        email_addr = users[user]["email"]
        while True:
            try:
                pickup = get_pickdate(model)
                if "Today" in pickup:
                    try:
                        logging.info("sending the email")
                        send_email(MSG_PICK, email_addr)
                    except Exception as e:
                        logging.error("MAIL Sending error. %s", e.message)
                        continue
            except Exception as e:
                logging.error(e.message)
                send_email(MSG_ERROR, email_addr)
                logging.error("waiting for solve")
                time.sleep(30 * 60)
    time.sleep(wait_time * 60)

main()






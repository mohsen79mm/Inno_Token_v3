from celery import shared_task
import time
import logging
from kavenegar import *
from sendsms import api


API_KEY = '4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D'
logger = logging.getLogger("django")


@shared_task(name="send_sms_code")
def send_sms_code(sender, phone, message):
    api = KavenegarAPI('4A7954397758375742704553337376623853334E6C446B61742B7947634D322B4A495A374A442F444A4B493D')
    time.sleep(5)
    try:
        params = { 'sender' : sender, 'receptor': phone, 'message' : message}
        api.sms_send(params)
    except Exception as e:
        logger.error("Send SMS codes [exception] [mobile:% s, message:% s]" % (mobile, e))
    else:
        if result == 0:
            logger.info("Send SMS codes [Success] [mobile:% s]" % mobile)
        else:
            logger.warning("Send SMS codes [Failure] [mobile:% s]" % mobile)
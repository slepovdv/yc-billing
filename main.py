import logging
import os
import sys
import time
from datetime import datetime, timedelta
from json import dumps

import json_logging
import schedule

import backet
import parsing_csv
import sheet
import tg

json_logging.init_non_web(enable_json=True)
logger = logging.getLogger('json-logger')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

costs = 0.0


def job():

    bucket = os.environ['BUCKET']
    yesterday = datetime.now() - timedelta(days=1)
    date_format = '%Y%m%d'

    data = backet.get_data(bucket, 'exp/' + yesterday.strftime(date_format) + '.csv')
    billing = round(parsing_csv.parse_csv(data), 2)

    date_format = '%d.%m.%Y'
    sheet.insert_data(yesterday.strftime(date_format), str(billing))

    global costs
    costs += billing
    if costs >= 20000.0:
        message = f'Затраты на облако привысили 20000 и составляют {costs} рублей\nСчетчик будет сброшен завтра'
        r = tg.send_tg_message(message)
        costs = 0.0
    else:
        message = f'Затраты на облако составляют {costs} рублей'
        r = tg.send_tg_message(message)

    logger.info(dumps(r))


schedule.every().day.at("04:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

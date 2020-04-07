import os

os.environ['DJANGO_SETTINGS_MODULE'] = 's4project.settings'

import django
import fxcmpy
from apscheduler.schedulers.blocking import BlockingScheduler

django.setup()
from investing.models import Price

sched = BlockingScheduler()
print("Scheduler created")
con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
con.subscribe_market_data('EUR/USD')
print("Connection started")


@sched.scheduled_job('interval', seconds=30)
def timed_job():
    if not con.is_subscribed('EUR/USD'):
        print('Connection to FXCMPY interrupted.')
    price = con.get_last_price('EUR/USD')
    Price(
        name='EUR/USD',
        bid=price['Bid'],
        ask=price['Ask'],
        high=price['High'],
        low=price['Low'],
        date=str(price.name.utcnow())) \
        .save()


print("Schedule started")
sched.start()
con.unsubscribe_market_data('EUR/USD')

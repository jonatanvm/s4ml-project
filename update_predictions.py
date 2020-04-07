import os

os.environ['DJANGO_SETTINGS_MODULE'] = 's4project.settings'

import django
from apscheduler.schedulers.blocking import BlockingScheduler

django.setup()
from investing.models import Price, Outcome, Prediction

sched = BlockingScheduler()
print("Scheduler created")
print("Connection started")


@sched.scheduled_job('interval', seconds=10)
def timed_job():
    predictions = Prediction.objects.filter(outcome__isnull=True).all()
    for prediction in predictions:
        price = Price.objects.filter(id=prediction.predictor).first()
        if price:
            Outcome(prediction=prediction, value=price.bid).save()


print("Schedule started")
sched.start()

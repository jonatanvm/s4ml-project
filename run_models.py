import json
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 's4project.settings'

import importlib.util
from timeit import default_timer as timer
import django
from apscheduler.schedulers.blocking import BlockingScheduler

django.setup()

from investing.models import Model, Price, Run, Prediction

sched = BlockingScheduler()
print("Model-runner created")


@sched.scheduled_job('interval', seconds=10)
def timed_job():
    data = list(Price.objects.values_list('id', 'bid').all()[:30])
    data.reverse()
    X, y = zip(*data)
    for model in Model.objects.filter(run_model=True).all():
        if model.type == 'T':
            print("Executing %s" % str(model))
            module_name = 'run_test'
            spec = importlib.util.spec_from_file_location(module_name, str(model.script))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            start = timer()
            rmse, mae, r2, profit, accuracy, parameters = module.run_test(y)
            end = timer()

            run = Run(model=model)
            run.rmse = rmse.item()
            run.mae = mae.item()
            run.r2 = r2.item()
            run.profit = profit.item()
            run.accuracy = accuracy.item()
            run.exec_time = end - start
            run.parameters = json.dumps(parameters)
            run.save()

        if model.type == 'P':
            if not Prediction.objects.filter(model=model, predictor=X[-1] + 1).first():
                module_name = 'predict'
                spec = importlib.util.spec_from_file_location(module_name, str(model.script))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                start = timer()
                prediction, parameters = module.predict(X, y, X[-1] + 1)
                end = timer()

                pred = Prediction(model=model, predictor=X[-1] + 1, value=prediction, exec_time=end - start)
                pred.save()
            else:
                print(f"Already predicted %s with model %s" % (X[-1] + 1, model))


print("Schedule started")
sched.start()

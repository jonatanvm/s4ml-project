# tutorial/tables.py
import json

import django_tables2 as tables
from django.utils.html import format_html
from django_tables2 import A

from .models import Model, Run, Prediction


class ModelTable(tables.Table):
    predictions = tables.LinkColumn('model_predictions', args=[A('id')], text='Predictions')
    test_runs = tables.LinkColumn('model_runs', args=[A('id')], text='Runs')
    edit = tables.LinkColumn("admin:investing_model_change", args=[A('id')], text='Edit')

    class Meta:
        model = Model
        template_name = "django_tables2/bootstrap.html"
        fields = ['id', 'name', 'script', 'run_model', 'created_on', 'modified_on', 'predictions', 'test_runs']


class RunTable(tables.Table):
    parameters = tables.Column()

    def render_parameters(self, value):
        d = json.loads(value)
        html = "".join(list([f"<p>{key}: {v}</p>" for key, v in d.items()]))
        return format_html(html)

    class Meta:
        model = Run
        template_name = "django_tables2/bootstrap.html"
        fields = ['id', 'rmse', 'mae', 'r2', 'profit', 'accuracy', 'exec_time', 'created_on', 'parameters']


class PredictionTable(tables.Table):
    true_value = tables.Column(accessor='get_outcome')
    class Meta:
        model = Prediction
        template_name = "django_tables2/bootstrap.html"
        fields = [f.name for f in Prediction._meta.fields] + ["true_value"]

from django.forms import ModelForm

from investing.models import Model


class MLModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'script', 'run_model', 'type']

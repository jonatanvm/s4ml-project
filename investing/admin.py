from django.contrib import admin

from .models import Price, Model, Run, Prediction, Outcome


# Register your models here.

@admin.register(Price)
class SettingsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Price._meta.fields]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Model._meta.fields]


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Run._meta.fields]


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Prediction._meta.fields]


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Outcome._meta.fields]

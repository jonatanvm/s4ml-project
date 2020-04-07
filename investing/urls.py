"""s4project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add/model', upload_model, name='add_model'),
    path('get/data/latest', get_latest_price_data),
    path('get/profit', get_profit),
    path('model/<int:id>/runs', runs, name='model_runs'),
    path('model/<int:id>/profit', get_profit, name='model_profit'),
    path('model/<int:id>/predictions', predictions, name='model_predictions'),
    path('study-log/<int:study_log_id>', study_log, name='study_log'),
    path('readme', readme, name='readme'),
    path('uploads/<path:file_path>', get_file, name='get_file')
]

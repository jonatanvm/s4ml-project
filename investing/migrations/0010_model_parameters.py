# Generated by Django 3.0.5 on 2020-04-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investing', '0009_auto_20200407_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='parameters',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investing', '0005_auto_20200406_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='ask',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='bid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='high',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='low',
            field=models.FloatField(),
        ),
    ]

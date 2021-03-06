# Generated by Django 3.0.5 on 2020-04-06 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investing', '0007_auto_20200406_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmse', models.DecimalField(decimal_places=5, default=0, max_digits=19)),
                ('mae', models.DecimalField(decimal_places=5, default=0, max_digits=19)),
                ('r2', models.DecimalField(decimal_places=5, default=0, max_digits=19)),
                ('profit', models.DecimalField(decimal_places=5, default=0, max_digits=19)),
                ('accuracy', models.DecimalField(decimal_places=5, default=0, max_digits=8)),
                ('exec_time', models.DecimalField(decimal_places=5, default=0, max_digits=19)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investing.Model')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-03-04 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foodfitnessApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodfitnessmodel',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='foodfitnessmodel',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 4, 17, 17, 49, 405247, tzinfo=utc)),
        ),
    ]

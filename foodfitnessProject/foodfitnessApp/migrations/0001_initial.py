# Generated by Django 2.2 on 2019-03-04 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodfitnessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('calories', models.IntegerField(default='')),
                ('date', models.DateField(default=datetime.datetime(2019, 3, 4, 16, 52, 20, 76381, tzinfo=utc))),
            ],
        ),
    ]

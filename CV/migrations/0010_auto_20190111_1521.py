# Generated by Django 2.1.3 on 2019-01-11 15:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0009_auto_20190108_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 11, 15, 21, 37, 38580, tzinfo=utc)),
        ),
    ]

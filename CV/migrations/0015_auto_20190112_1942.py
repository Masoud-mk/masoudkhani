# Generated by Django 2.1.3 on 2019-01-12 19:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0014_auto_20190112_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='cv',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 12, 19, 42, 26, 569296, tzinfo=utc)),
        ),
    ]

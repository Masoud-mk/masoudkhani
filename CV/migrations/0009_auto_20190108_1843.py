# Generated by Django 2.1.3 on 2019-01-08 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0008_auto_20190106_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refrences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 8, 18, 43, 6, 876700, tzinfo=utc)),
        ),
    ]

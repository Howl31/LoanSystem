# Generated by Django 3.1.4 on 2020-12-29 07:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_myuser_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_issue',
            field=models.DateField(default=datetime.datetime(2020, 12, 29, 7, 49, 53, 33048, tzinfo=utc)),
        ),
    ]

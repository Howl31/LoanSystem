# Generated by Django 3.1.4 on 2020-12-29 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_auto_20201229_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalteam',
            name='due_date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalteam',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalteam',
            name='final_rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_issue',
            field=models.DateField(default=datetime.datetime(2020, 12, 29, 12, 4, 4, 787406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]

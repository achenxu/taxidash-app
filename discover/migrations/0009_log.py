# Generated by Django 2.0 on 2019-10-30 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0008_remove_trip_meetup_pt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date')),
                ('activity', models.CharField(max_length=2000)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-12-23 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplans', '0017_customerregisteredplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerregisteredplan',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 23, 15, 48, 47, 546517, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]

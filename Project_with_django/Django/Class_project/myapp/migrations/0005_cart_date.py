# Generated by Django 4.2.5 on 2023-11-25 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_cart_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 4, 1, 40, 935951, tzinfo=datetime.timezone.utc)),
        ),
    ]

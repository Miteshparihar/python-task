# Generated by Django 4.2.5 on 2023-11-28 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_cart_date_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 11, 9, 57, 233339, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 11, 9, 57, 233339, tzinfo=datetime.timezone.utc)),
        ),
    ]

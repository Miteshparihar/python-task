# Generated by Django 4.2.5 on 2023-11-25 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart_razorpay_order_id_cart_razorpay_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 9, 27, 33, 995859, tzinfo=datetime.timezone.utc)),
        ),
    ]

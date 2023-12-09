# Generated by Django 4.2.5 on 2023-11-28 08:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cart_razorpay_order_id_cart_razorpay_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 8, 32, 53, 637224, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand_amount', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 11, 28, 8, 32, 53, 637224, tzinfo=datetime.timezone.utc))),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
            ],
        ),
    ]

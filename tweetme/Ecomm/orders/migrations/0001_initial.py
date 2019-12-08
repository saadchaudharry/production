# Generated by Django 2.2 on 2019-11-15 11:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0004_address_contact_no'),
        ('products', '0031_auto_20191015_1532'),
        ('carts', '__first__'),
        ('billing', '0003_blilling_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded'), ('delivered', 'Delivered'), ('cancel', 'Cancel')], default='created', max_length=120)),
                ('state', models.CharField(blank=True, choices=[('c_delete', 'c_delete'), ('o_delete', 'o_delete')], default=None, max_length=120, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('active', models.BooleanField(default=True)),
                ('billing_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.Blilling')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.Cart')),
                ('prods', models.ManyToManyField(blank=True, to='products.Product')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.Address')),
            ],
        ),
    ]

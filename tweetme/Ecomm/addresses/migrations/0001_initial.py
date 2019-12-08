# Generated by Django 2.2 on 2019-10-27 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0003_blilling_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_1', models.CharField(max_length=120)),
                ('address_2', models.CharField(max_length=120)),
                ('country', models.CharField(default='India', max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('pin_code', models.IntegerField(max_length=120)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.Blilling')),
            ],
        ),
    ]

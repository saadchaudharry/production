# Generated by Django 2.2 on 2019-10-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20191028_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

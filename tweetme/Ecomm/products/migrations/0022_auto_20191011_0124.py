# Generated by Django 2.2 on 2019-10-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20191011_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('cats', 'Cat'), ('dogs', 'Dog'), ('birds', 'Bird'), ('featured', 'Featured'), ('fish', 'Fishes'), ('accessories', 'Accessories')], default=None, max_length=120),
        ),
    ]

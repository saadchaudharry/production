# Generated by Django 2.2 on 2019-10-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20191010_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('fishes', 'Fish'), ('cats', 'Cat'), ('dogs', 'Dog'), ('birds', 'Bird'), ('featured', 'Featured')], default='fishes', max_length=120),
        ),
    ]

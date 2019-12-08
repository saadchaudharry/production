# Generated by Django 2.2 on 2019-10-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20191009_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bird',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dog',
        ),
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fish',
        ),
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('fi', 'Fish'), ('ca', 'Cat'), ('do', 'Dog'), ('bi', 'Bird'), ('fe', 'Featured'), ('ot', 'Other')], default='fi', max_length=120),
        ),
    ]
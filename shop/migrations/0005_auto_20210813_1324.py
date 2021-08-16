# Generated by Django 3.1.5 on 2021-08-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_sale_date_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='item_unit',
            field=models.CharField(default='Kg', max_length=20),
        ),
        migrations.AddField(
            model_name='stock',
            name='item_unit',
            field=models.CharField(default='Kg', max_length=20),
        ),
    ]
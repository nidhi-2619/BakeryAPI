# Generated by Django 4.2.2 on 2023-07-04 14:03

import Bakery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bakery', '0008_ingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakeryitemingredient',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name=Bakery.models.Ingredient),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bakery', '0006_remove_ingredient_quantity_percentage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryBakeryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(auto_created=True, default=0)),
                ('bakery_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.bakeryitem')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(auto_created=True, default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.ingredient')),
            ],
        ),
        migrations.AlterField(
            model_name='bakeryitemingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='quantity', to='Bakery.ingredient'),
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]

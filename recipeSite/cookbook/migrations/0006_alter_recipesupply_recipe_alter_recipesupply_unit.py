# Generated by Django 4.2.5 on 2023-09-16 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_alter_recipeinstruction_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesupply',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipeSupplies', to='cookbook.recipe'),
        ),
        migrations.AlterField(
            model_name='recipesupply',
            name='unit',
            field=models.TextField(blank=True, null=True),
        ),
    ]

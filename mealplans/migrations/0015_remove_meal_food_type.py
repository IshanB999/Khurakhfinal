# Generated by Django 5.1.2 on 2024-12-23 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealplans', '0014_meal_food_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='food_type',
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-14 12:18

from django.db import migrations

import json


def push_ingredients(apps, schema_editor):
    with open('/code/ingredients.json', encoding='utf-8') as f:
        data = json.load(f)

    Ingredient = apps.get_model('recipes', 'Ingredient')
    if Ingredient.objects.exists():
        return
    ingredients = []
    for ing in data:
        ingredients.append(Ingredient(name=ing['name'], unit=ing['unit']))
    Ingredient.objects.bulk_create(ingredients)


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0009_auto_20200913_1207'),
    ]

    operations = [
        migrations.RunPython(push_ingredients)
    ]

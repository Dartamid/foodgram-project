from django.db import migrations
import json


def code(apps, schema_editor):
    Ingredient = apps.get_model('recipes', 'Ingredient')

    with open('ingredients.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    for ingredient in data:
        Ingredient.objects.get_or_create(
            title=ingredient['title'],
            defaults={"dimension": ingredient['dimension']}
        )


def reverse_code(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code, reverse_code=reverse_code),
    ]

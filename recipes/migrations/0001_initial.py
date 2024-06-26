from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('dimension', models.CharField(max_length=50, verbose_name='Единицы измерения')),
            ],
            options={
                'verbose_name': 'Ингридиент',
                'verbose_name_plural': 'Ингридиенты',
            },
        ),
        migrations.CreateModel(
            name='IngredientValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_values', to='recipes.Ingredient', verbose_name='Ингридиент')),
            ],
            options={
                'verbose_name': 'Количество ингридиентов',
                'verbose_name_plural': 'Количество ингридиентов',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('breakfast', models.BooleanField(verbose_name='Завтрак')),
                ('lunch', models.BooleanField(verbose_name='Обед')),
                ('dinner', models.BooleanField(verbose_name='Ужин')),
                ('cooking_time', models.PositiveSmallIntegerField(verbose_name='Время приготовления')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Фото')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('ingredients', models.ManyToManyField(through='recipes.IngredientValue', to='recipes.Ingredient', verbose_name='Ингридиенты')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AddField(
            model_name='ingredientvalue',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_values', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
    ]

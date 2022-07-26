# Generated by Django 3.2.13 on 2022-06-12 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Актер')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_actors/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Категория')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Режиссеры')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_directors/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Жанр')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='logo', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Лого',
                'verbose_name_plural': 'Лого',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slogan', models.CharField(blank=True, max_length=70, verbose_name='Слоган')),
                ('poster', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('budget', models.PositiveIntegerField(default=0, verbose_name='Бюджет')),
                ('draft', models.BooleanField(default=True, verbose_name='Публикация')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('actors', models.ManyToManyField(related_name='movie_actor', to='movies.Actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='movie_directors', to='movies.Director', verbose_name='Режиссеры')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
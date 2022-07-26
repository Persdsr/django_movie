from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.urls import reverse
from .middleware import get_current_user
from django.db.models import Q


class Logo(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    photo = models.ImageField(verbose_name='Изображение', upload_to='logo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лого'
        verbose_name_plural = 'Лого'


class Movies(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание')
    slogan = models.CharField(verbose_name='Слоган', blank=True, max_length=70)
    poster = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    year = models.PositiveSmallIntegerField(verbose_name='Год выхода', null=True)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', null=True)
    country = models.CharField(verbose_name='Страна', max_length=30)
    actors = models.ManyToManyField('Actor', verbose_name='Актеры', related_name='movie_actor')
    directors = models.ManyToManyField('Director', verbose_name='Режиссеры', related_name='movie_directors')
    budget = models.PositiveIntegerField(verbose_name='Бюджет', default=0)
    genres = models.ManyToManyField('Genre', verbose_name='Жанр')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField(verbose_name='Публикация', default=True)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True)
    video = models.FileField(verbose_name='Видео', upload_to='video', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['id']

class StatusFilterComments(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=False)


class Comments(models.Model):
    article = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='Кино', blank=True, null=True, related_name='comments_movies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    status = models.BooleanField(verbose_name='Видимость комментария', default=False)
    objects = StatusFilterComments()

    def __str__(self):
        return f"{self.article} - {self.author}"

    class Meta:
        ordering = ['-create_date']

class Actor(models.Model):
    name = models.CharField(verbose_name='Актер', max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='image_actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Director(models.Model):
    name = models.CharField(verbose_name='Режиссеры', max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='image_directors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=30)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=15)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contact(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=55)
    email = models.EmailField(verbose_name='Почта', max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



# Generated by Django 3.2.13 on 2022-06-14 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['id'], 'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]

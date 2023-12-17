# Generated by Django 4.2.8 on 2023-12-17 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('image', models.ImageField(upload_to='movies/', verbose_name='Добавьте фото')),
                ('description', models.TextField(blank=True, verbose_name='Описание фильма')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(2500)], verbose_name='Укажите цену')),
                ('genre', models.CharField(choices=[('Аниме', 'Аниме'), ('Исторический', 'Исторический'), ('Боевик', 'Боевик'), ('Детектив', 'Детектив'), ('Криминал', 'Криминал'), ('Ужасы', 'Ужасы'), ('Мелодрама', 'Мелодрама'), ('Фантастика', 'Фантастика')], max_length=100)),
                ('author', models.TextField(max_length=1000, verbose_name='Авторы фильма')),
                ('trailer', models.URLField(blank=True, verbose_name='Ссылка на трейлер фильма')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

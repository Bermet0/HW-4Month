from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    Genre = (
        ('Аниме', 'Аниме'),
        ('Исторический', 'Исторический'),
        ('Боевик', 'Боевик'),
        ('Детектив', 'Детектив'),
        ('Криминал', 'Криминал'),
        ('Ужасы', 'Ужасы'),
        ('Мелодрама', 'Мелодрама'),
        ('Фантастика', 'Фантастика')
    )
    movie_title = models.CharField(max_length=100, verbose_name='Название фильма', null=True)
    movie_image = models.ImageField(upload_to='movies/', verbose_name='Добавьте фото', null=True)
    movie_description = models.TextField(verbose_name='Описание фильма', blank=True, null=True)
    movie_price = models.PositiveIntegerField(verbose_name='Укажите цену',
                                              validators=[MinValueValidator(100),
                                                          MaxValueValidator(2500)], null=True)
    movie_genre = models.CharField(max_length=100, choices=Genre, null=True)
    movie_author = models.TextField(max_length=1000, verbose_name='Авторы фильма', null=True)
    movie_trailer = models.URLField(verbose_name='Ссылка на трейлер фильма', blank=True, null=True)
    movie_created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.movie_title


class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment

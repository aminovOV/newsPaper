from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.user.username

    def update_rating(self):
        post_rate = self.post_set.aggregate(post_rating=Sum('rating'))
        rate = 0
        rate += post_rate.get('post_rating')
        comment_rate = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        c_rate = 0
        c_rate += comment_rate.get('comment_rating')
        self.rating = rate*3 + c_rate
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название категории')
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_TYPES = (
        ('N', 'Новость'),
        ('A', 'Статья'),
    )
    post_type = models.CharField(max_length=1, choices=POST_TYPES, verbose_name='Тип новости')
    headline = models.CharField(max_length=255, verbose_name='Заголовок')
    body_text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.headline}, {self.pub_date}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.body_text[0:124]}...'
    preview.short_description = 'Превью'

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

    def display_category(self):
        return ', '.join([category.name for category in self.category.all()[:3]])
    display_category.short_description = 'Категория'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикации'

    def __str__(self):
        return f'{self.category.name}'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Публикация')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    
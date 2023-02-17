from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        post_rate = self.post_set.aggregate(post_rating=Sum('rating'))
        rate = 0
        rate += post_rate.get('post_rating')
        # comment_rate = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        # c_rate = 0
        # c_rate += comment_rate.get('comm_rating')
        self.rating = rate*3  # + c_rate. 'User' object has no attribute 'comments_set'
        return self.rating


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_TYPES = (
        ('N', 'News'),
        ('A', 'Article'),
    )
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.body_text[0:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

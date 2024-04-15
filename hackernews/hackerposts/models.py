from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    nickname = models.CharField(max_length=25, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255, unique=True)


class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    root_comment_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    parent_comment_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

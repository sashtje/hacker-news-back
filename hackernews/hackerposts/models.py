from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    nickname = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]


class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    rootcomment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='root')
    parentcomment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='parent')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]

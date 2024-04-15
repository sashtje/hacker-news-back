from rest_framework import serializers
from .models import Post, Author, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author_nickname = serializers.CharField(source='author.nickname')

    class Meta:
        model = Post
        fields = ('id', 'title', 'rating', 'created_at', 'url', 'author_nickname')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

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


class CommentRootSerializer(serializers.ModelSerializer):
    author_nickname = serializers.CharField(source='author.nickname')
    comments_count = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'text', 'author_nickname', 'comments_count')


class CommentSerializer(serializers.ModelSerializer):
    author_nickname = serializers.CharField(source='author.nickname')

    class Meta:
        model = Comment
        fields = ('id', 'created_at', 'text', 'parentcomment_id', 'rootcomment_id', 'author_nickname')

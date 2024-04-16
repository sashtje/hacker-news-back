from django.db.models import Count, OuterRef, Subquery
from django.db.models.functions import Coalesce
from rest_framework import generics

from .serializers import PostSerializer, CommentRootSerializer, CommentSerializer
from .models import Post, Comment


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:100].select_related('author')
    serializer_class = PostSerializer


class CommentRootAPIView(generics.ListAPIView):
    serializer_class = CommentRootSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']

        queryset1 = Comment.objects.filter(post_id=post_id, rootcomment_id=None).select_related('author')

        queryset2 = Comment.objects.filter(post_id=post_id, rootcomment_id__isnull=False) \
            .values('rootcomment') \
            .annotate(count=Count('id'))

        combined_queryset = queryset1.annotate(
            comments_count=Coalesce(Subquery(queryset2.filter(rootcomment=OuterRef('id')).values('count')[:1]), 0)
        )
        return combined_queryset


class CommentAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        root_id = self.kwargs['root_id']
        queryset = Comment.objects.filter(post_id=post_id, rootcomment_id=root_id).select_related('author')
        return queryset

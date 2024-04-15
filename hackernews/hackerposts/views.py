from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:100].select_related('author')
    serializer_class = PostSerializer

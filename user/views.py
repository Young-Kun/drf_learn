from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, mixins
from rest_framework.mixins import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

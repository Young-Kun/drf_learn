from .models import Post, User, Topic
from .serializers import PostSerializer, UserSerializer, TopicSerializer
from rest_framework import viewsets, permissions, serializers, settings
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    '''
    fdasfdsafsaddfadas
    create: 返回文章列表
    list: 发大水发大水
    retrieve: 获得一个
    put: 修改一个
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

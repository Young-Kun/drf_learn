from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'topics', views.TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

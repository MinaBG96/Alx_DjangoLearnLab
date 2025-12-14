from rest_framework.routers import DefaultRouter
# from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FeedView
from .views import LikePostView, UnlikePostView

# router = DefaultRouter()
# router.register(r'posts', PostViewSet)
# router.register(r'comments', CommentViewSet)

urlpatterns =[
    path('feed/', FeedView.as_view()),
    path('posts/<int:pk>/like/', LikePostView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view()),
]
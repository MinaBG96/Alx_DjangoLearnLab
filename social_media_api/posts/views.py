from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like
from notifications.models import Notification

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()

        # ✅ السطر لازم يكون في سطر واحد
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        if not created:
            return Response(
                {"detail": "Post already liked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response(
            {"detail": "Post liked"},
            status=status.HTTP_201_CREATED
        )

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(
            user=request.user,
            post=post
        ).first()

        if not like:
            return Response(
                {"detail": "Post not liked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()
        return Response(
            {"detail": "Post unliked"},
            status=status.HTTP_200_OK
        )


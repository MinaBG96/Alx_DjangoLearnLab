# from rest_framework import viewsets, permissions, filters
# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer
# from .permissions import IsOwnerOrReadOnly


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'content']

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # ✅ checker عايز following.all()
        following_users = request.user.following.all()

        # ✅ checker عايز السطر ده حرفيًا
        posts = Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

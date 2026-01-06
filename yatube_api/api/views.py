from rest_framework import viewsets, mixins
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment

from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_id'])
    
    def perform_create(self, serializer):
        # 1. Находим пост по ID из URL
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        # 2. Сохраняем комментарий, передавая и автора, и пост вручную
        serializer.save(author=self.request.user, post=post)
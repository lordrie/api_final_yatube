from posts.models import Post, Group
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from django.shortcuts import get_object_or_404
from .permissions import OwnerOrReadOnly, GroupOnlyGet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.exceptions import ValidationError
from posts.models import Follow


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Comment."""
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с моделью Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (GroupOnlyGet,)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        following = serializer.validated_data.get('following')
        user = self.request.user
        if user == following:
            raise ValidationError('Вы не можете подписаться на самого себя.', code=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(user=user, following=following).exists():
            raise ValidationError('Вы уже подписаны на этого пользователя.', code=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user)

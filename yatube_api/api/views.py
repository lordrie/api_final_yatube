from posts.models import Post, Group
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с моделью Comment."""
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_post(self, post_id):
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post(self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        """Создает комментарий, связывая его с автором и постом"""
        post = self.get_post(self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с моделью Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.GenericViewSet,
                    CreateModelMixin, ListModelMixin):
    """Вьюсет для работы с моделью Follow."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

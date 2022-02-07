from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, viewsets
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly
from blog.models import Post
from .serializers import PostSerializer

class PostUserWritePermission(BasePermission):
  message = "Editing posts is restricted to the author only."

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
      
    return obj.author == request.user

class PostList(viewsets.ModelViewSet):
  permission_classes = [PostUserWritePermission]
  serializer_class = PostSerializer
  filterset_fields = ['slug']
  search_fields = ['slug']

  def get_object(self):
      item = self.kwargs.get('pk')
      return get_object_or_404(Post, slug=item)

  def get_queryset(self):
    return Post.postobjects.all()
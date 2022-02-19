from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from blog.models import Category, Post
from .serializers import CategorySerializer, PostSerializer

class PostUserWritePermission(BasePermission):
  message = "Editing posts is restricted to the author only."

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
      
    return obj.author == request.user
  

class PostList(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filterset_fields = ['slug', 'category']
  search_fields = ['slug']

  def get_queryset(self):
      return Post.objects.filter(status='published')


class PostDetail(generics.RetrieveAPIView):
  serializer_class = PostSerializer

  def get_object(self):
    slug = self.kwargs.get('slug')
    return get_object_or_404(Post, slug=slug)


class UserPostList(generics.ListAPIView):
  serializer_class = PostSerializer

  def get_queryset(self):
    user = self.request.user
    return Post.objects.filter(author=user)

# class CreatePost(generics.CreateAPIView):
#   permission_classes = [IsAuthenticated]
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

#   def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     try:
#       self.perform_create(serializer)
#     except ValidationError as e:
#       raise ValidationError(e.messages)
    
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#   def perform_create(self, serializer):
#    return serializer.save(author=self.request.user)
   

class CreatePost(APIView):
  permission_classes = [IsAuthenticated]
  parser_classes = [MultiPartParser, FormParser]

  def post(self, request, format=None):
    print(request.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AdminPostDetail(generics.RetrieveAPIView):
  permission_classes = [PostUserWritePermission]
  serializer_class = PostSerializer

  def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, id=item)


class EditPost(generics.RetrieveUpdateAPIView):
  permission_classes = [PostUserWritePermission]
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class DeletePost(generics.DestroyAPIView):
  permission_classes = [PostUserWritePermission]
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class CategoryList(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  search_fields = ['name']


class CreateCategory(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class AdminCategoryDetail(generics.RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class EditCategory(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class DeleteCategory(generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
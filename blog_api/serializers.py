from rest_framework.serializers import ModelSerializer

from blog.models import Category, Post
from users.serializers import UserSerializer

class PostSerializer(ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'title', 'author', 'category', 'image', 'excerpt', 'content', 'status', 'slug']

  def to_representation(self, instance):
    rep = super().to_representation(instance)
    rep['author'] = UserSerializer(instance.author).data
    rep['category'] = CategorySerializer(instance.category).data
    return rep

class CategorySerializer(ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']
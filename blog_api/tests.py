from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from blog.models import Category, Post

class PostTests(APITestCase):
  def test_view_posts(self):
    url = reverse('blog_api:post_list')
    response = self.client.get(url, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_create_post(self):
    self.test_category = Category.objects.create(name='django')
    self.test_user1 = User.objects.create_user(username='test_user1', password='123456789')

    self.client.login(username='test_user1', password='123456789')

    data = {'title': 'new', 'author': 1, 'excerpt': 'new', 'content': 'new'}
    url = reverse('blog_api:post_list')
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    root = reverse(('blog_api:post_detail'), kwargs={'pk': 1})
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_update_post(self):
    client = APIClient()

    self.test_category = Category.objects.create(name='django')
    self.test_user1 = User.objects.create_user(username='test_user1', password='123456789')
    self.test_user2 = User.objects.create_user(username='test_user2', password='123456789')

    test_post = Post.objects.create(category_id=1, title='Post title', content='Post content', excerpt='Post excerpt', slug='post-title', author_id=1, status='published')

    client.login(username='test_user2', password='123456789')

    url = reverse(('blog_api:post_detail'), kwargs={'pk': 1})
    data = {'title': 'new', 'author': 1, 'excerpt': 'new', 'content': 'new', 'status': 'published'}
    response = client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    client.logout()

    client.login(username='test_user1', password='123456789')
    response = client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

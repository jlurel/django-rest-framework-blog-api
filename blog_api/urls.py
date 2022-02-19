
from django.urls import path
from .views import AdminCategoryDetail, AdminPostDetail, CategoryList, CreateCategory, CreatePost, DeleteCategory, DeletePost, EditCategory, EditPost, PostDetail, PostList, UserPostList

app_name = "blog_api"

urlpatterns = [
  path('posts', PostList.as_view(), name='list_posts'),
  path('posts/admin', UserPostList.as_view(), name='admin_posts'),
  path('posts/<str:slug>', PostDetail.as_view(), name='detail_post'),
  path('posts/admin/create', CreatePost.as_view(), name='create_post'),
  path('posts/admin/<int:pk>', AdminPostDetail.as_view(), name='admin_post'),
  path('posts/admin/<int:pk>/edit', EditPost.as_view(), name='edit_post'),
  path('posts/admin/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
  path('categories', CategoryList.as_view(), name='list_categories'),
  path('categories/admin/create', CreateCategory.as_view(), name='create_category'),
  path('categories/admin/<int:pk>', AdminCategoryDetail.as_view(), name='admin_category'),
  path('categories/admin/<int:pk>/edit', EditCategory.as_view(), name='edit_category'),
  path('categories/admin/<int:pk>/delete', DeleteCategory.as_view(), name='delete_category')
]




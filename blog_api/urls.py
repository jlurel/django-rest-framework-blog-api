
from rest_framework.routers import DefaultRouter
from .views import CategoryList, PostList

app_name = "blog_api"

router = DefaultRouter()
router.register('posts', PostList, basename='posts')
router.register('categories', CategoryList, basename='categories')
urlpatterns = router.urls



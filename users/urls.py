from django.urls import path
from .views import BlacklistTokenView, CustomUserCreate, UserAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('profile', UserAPIView.as_view(), name='auth_get_profile'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', CustomUserCreate.as_view(), name='auth_register'),
    path('logout', BlacklistTokenView.as_view(), name='auth_logout')
]

from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterUserSerializer, UserSerializer

class UserAPIView(RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = UserSerializer

  def get_object(self):
      return self.request.user


class CustomUserCreate(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    reg_serializer = RegisterUserSerializer(data=request.data)
    if reg_serializer.is_valid():
      new_user = reg_serializer.save()
      if new_user:
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    try:
      refresh_token = request.data["refresh_token"]
      token = RefreshToken(refresh_token)
      token.blacklist()
      return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)
from asyncore import write
from rest_framework import serializers
from .models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True)
  user_name = serializers.CharField(required=True)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = NewUser
    fields = ('email', 'user_name', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    
    if password is not None:
      instance.set_password(password)
    instance.save()

    return instance

class UserSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user_name')
  firstname = serializers.CharField(source='first_name')

  class Meta:
    model = NewUser
    fields = ('id', 'email', 'username', 'firstname', 'about')
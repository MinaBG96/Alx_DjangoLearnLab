from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ CharField موجودة

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # ✅ create_user بالضبط
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
        )

        user.bio = validated_data.get('bio', '')
        user.save()

        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture']

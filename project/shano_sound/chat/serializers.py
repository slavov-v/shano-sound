from rest_framework import serializers
from user_management.models import User


class OnlineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_online')

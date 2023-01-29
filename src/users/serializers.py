from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from rest_framework import serializers

User = get_user_model()


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name", "codename")


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ("name", "permissions")


class UserSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"

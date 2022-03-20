from djoser.conf import settings
from djoser.serializers import UserSerializer
from rest_framework import serializers

from authentication.models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "pk",
            "first_name",
            "last_name",
            "student_code",
            "career",
        )


class CustomUserSerializer(UserSerializer):
    profile = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            "profile",
        )
        read_only_fields = (settings.LOGIN_FIELD,)

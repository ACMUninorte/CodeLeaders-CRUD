from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from authentication.models import Profile
from authentication.serializers import ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = "profile-detail"

    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user.profile

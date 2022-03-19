from django.urls.conf import path
from djoser.views import UserViewSet

urlpatterns = [
    path("send_reset_pass_email/", UserViewSet.as_view({"post": "reset_password"})),
]

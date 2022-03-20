from django.urls.conf import path
from djoser.views import UserViewSet

from authentication import views

urlpatterns = [
    path("send_password_reset_email/", UserViewSet.as_view({"post": "reset_password"})),
    path("reset_password/", UserViewSet.as_view({"post": "reset_password_confirm"})),
    path("me/", UserViewSet.as_view({"get": "me"})),
    path("profile/", views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
]

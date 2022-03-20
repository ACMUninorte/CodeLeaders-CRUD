from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsCurrentUserOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user

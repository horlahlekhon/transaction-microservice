import json

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from microservice.models import Clients
from django.core.exceptions import ObjectDoesNotExist


class IsAuthenticated(permissions.BasePermission):
    message = {"Details": "Authentication credentials was not provided or The provided one does not exist"}

    def has_permission(self, request, view) -> bool:
        key = request.META.get("x-api-key")
        api_key = request.headers.get("x-api-key") if not key else key
        try:
            valid = Clients.objects.get(api_key=api_key)
            return valid is not None
        except Exception as reason:
            raise PermissionDenied({"Details": "Authentication credentials was not provided or The provided one does "
                                               "not exist"})

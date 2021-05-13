import hashlib
import json
from typing import Any, Dict

from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse, HttpResponse
from rest_framework import status


class CacheMiddleware(MiddlewareMixin):

    def digest(self, data: Dict[str, Any]) -> str:
        dhash = hashlib.md5()
        encoded = json.dumps(data, sort_keys=True).encode()
        dhash.update(encoded)
        return dhash.hexdigest()

    def process_request(self, request):
        cache_ctrl = request.META.get("Cache-Control") or request.headers.get("Cache-Control")
        if cache_ctrl != "No-Cache":
            body = json.loads(request.body)
            body_hash = self.digest(body)
            cachee = cache.get(body_hash)
            if cachee:
                print("already cached")
                return cachee
            print("new request moving to view")
        else:
            print(f"caching seems to be disabled: {cache_ctrl}")

    def process_response(self, request, response):
        if response.status_code == status.HTTP_200_OK:
            body = json.loads(request.body)
            body_hash = self.digest(body)
            cache.set(body_hash, response)
        return response

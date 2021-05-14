import json
import logging
from collections import ItemsView

from django.utils.deprecation import MiddlewareMixin

from microservice.models import RequestLogs


class RequestLoggingMiddleware(MiddlewareMixin):

    @property
    def log(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel("DEBUG")
        return logger

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_response(self, request, response):
        try:
            ip = self.get_client_ip(request)
            body = json.loads(request.body)
            meta = {**request.headers}
            method = request.META.get("REQUEST_METHOD")
            path = request.META.get("PATH_INFO")
            c_type = request.META.get("CONTENT_TYPE")
            c_len  = request.META.get("CONTENT_LENGTH")
            RequestLogs.objects.create(ip=ip, method=method, content_type=c_type,
                                       content_length=c_len, request_body=body,
                                       request_headers=meta, path=path, response_body=response.data)
            return response
        except Exception as reason:
            self.log.exception(f"An exception occur while logginng request data: caused by {reason}")
            return response
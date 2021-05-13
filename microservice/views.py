# Create your views here.
import requests
from requests import HTTPError
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from microservice.models import Clients
from microservice.serializers import TransactionSerializer
from microservice.permissions import IsAuthenticated


class TransactionsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def call_webhook(self, client: Clients, payload: dict):
        requests.post(client.webhook_url, data=payload).raise_for_status()
        return True

    def get_object(self):
        key = self.request.headers.get("x-api-key") or self.request.META.get("x-api-key")
        return get_object_or_404(Clients.objects.all(), api_key=key)

    def post(self, request, *args, **kwargs):
        print(f"request headers:{request.headers}")
        serializer = self.get_serializer_class()
        ser = serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        client = self.get_object()
        tx = ser.save(client=client)
        try:
            payload = {
                "transaction_reference": tx.transaction_reference,
                "status": tx.status
            }
            self.call_webhook(client, payload)
        except Exception as reason:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                      "error": f"Sorry, webhook request cannot be processed, due to {reason.args}",
                      "transaction_id": tx.id,
                      "transaction_reference": tx.transaction_reference
                      }
            )
        return Response(status=status.HTTP_200_OK)

import json
import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from microservice.models import Clients, Transactions


class TestTransactionCreateView(APITestCase):
    def setUp(self) -> None:
        self.cliente = Clients.objects.create(webhook_url="http://www.google.com", api_key="key", name="client_1")

    def test_create_transaction(self):
        data = {
            "transaction_reference": str(uuid.uuid4()),
            "price": 234.10,
            "status": "successful"
        }
        opts = {
            "data": json.dumps(data), "content_type": "application/json", "x-api-key": self.cliente.api_key
        }
        resp = self.client.post(reverse("create_transactions"), **opts)
        tx = Transactions.objects.filter(transaction_reference=data["transaction_reference"])
        self.assertEqual(len(tx), 1)

    def test_create_tx_fail_unauthenticated(self):
        data = {
            "transaction_reference": str(uuid.uuid4()),
            "price": 234.10,
            "status": "successful"
        }
        opts = {
            "data": json.dumps(data), "content_type": "application/json"
        }
        resp = self.client.post(reverse("create_transactions"), **opts)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        tx = Transactions.objects.filter(transaction_reference=data["transaction_reference"])
        self.assertEqual(len(tx), 0)

    def test_create_tx_fail_404_with_client_not_found(self):
        data = {
            "transaction_reference": str(uuid.uuid4()),
            "price": 234.10,
            "status": "successful"
        }

        opts = {
            "data": json.dumps(data), "content_type": "application/json", "x-api-key": "wrong_key"
        }
        resp = self.client.post(reverse("create_transactions"), **opts)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        tx = Transactions.objects.filter(transaction_reference=data["transaction_reference"])
        self.assertEqual(len(tx), 0)

    def test_create_tx_fail_with_wrong_payload(self):
        data = {
            "transaction_reference": str(uuid.uuid4()),
            "status": "successful"
        }
        opts = {
            "data": json.dumps(data), "content_type": "application/json", "x-api-key": self.cliente.api_key
        }
        resp = self.client.post(reverse("create_transactions"), **opts)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        tx = Transactions.objects.filter(transaction_reference=data["transaction_reference"])
        self.assertEqual(len(tx), 0)

import binascii
import json
import os

from django.core.management import BaseCommand

from microservice.models import Clients


class Command(BaseCommand):
    help = "Create two default clients"

    def handle(self, *args, **options):
        with open("clients.json", 'r') as clients:
            data = json.loads(clients.read())
            var = [Clients.objects.create(id=index +1,
                                          api_key=binascii.hexlify(os.urandom(24)).decode(encoding="utf-8"),
                                          **d) for index, d in enumerate(data)]
            print(f"seeded : {len(var)} of clients")
            # Clients.objects.create(id=1,name="client_1", api_key=binascii.hexlify(os.urandom(24)).decode(encoding="utf-8"), webhook_url="google.com")
            # Clients.objects.create(id=2,name="client_2", api_key=binascii.hexlify(os.urandom(24)).decode(encoding="utf-8"), webhook_url="google.com")
            # Clients.objects.create(id=3,name="client_3", api_key=binascii.hexlify(os.urandom(24)).decode(encoding="utf-8"), webhook_url="google.com")

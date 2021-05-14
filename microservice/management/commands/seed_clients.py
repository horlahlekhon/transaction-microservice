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
            var = [Clients.objects.create(api_key=binascii.hexlify(os.urandom(24)).decode(encoding="utf-8"),
                                          **d) for index, d in enumerate(data)]
            print(f"seeded : {len(var)} of clients")

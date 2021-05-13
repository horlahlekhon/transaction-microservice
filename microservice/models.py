from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models


# Create your models here.

class Transactions(models.Model):
    class TransactionStatus(models.TextChoices):
        Successful = "successful", _("completed transaction")
        Pending = "pending", _("pending transaction")
        Failed = "failed", _("failed transaction")

    id = models.AutoField(primary_key=True)
    transaction_reference = models.CharField(max_length=100, null=False, blank=False, unique=True)
    price = models.DecimalField(decimal_places=4, max_digits=10)
    client = models.ForeignKey("Clients", on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=TransactionStatus.choices,
                              max_length=10, null=False, blank=False, default=TransactionStatus.Successful)


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    webhook_url = models.URLField()
    api_key = models.CharField(max_length=50)

    def __str__(self):
        return f"Client(id = {self.id}, name = {self.name}, webhook_url = {self.webhook_url}, api_key = {self.api_key})"


class RequestLogs(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=10,null=True, blank=True)
    content_length = models.IntegerField(null=True, blank=True)
    content_type = models.CharField(max_length=50, null=True, blank=True)
    request_body = models.JSONField(null=True, blank=True)
    request_headers = models.JSONField(null=True, blank=True)
    path = models.CharField(max_length=50, null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)

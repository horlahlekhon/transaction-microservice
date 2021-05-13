
from rest_framework import serializers

from microservice.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    transaction_reference = serializers.CharField(required=True)
    price = serializers.DecimalField(decimal_places=4, max_digits=10)
    created_at = serializers.DateTimeField(required=False)
    client = serializers.IntegerField(required=False)
    status = serializers.ChoiceField(choices=Transactions.TransactionStatus.choices, required=False)

    class Meta:
        model = Transactions
        fields = "__all__"

    def create(self, validated_data):
        ref = validated_data.get("transaction_reference")
        exists = Transactions.objects.filter(transaction_reference=ref)
        if len(exists) != 0:
            return exists[0]
        return super(TransactionSerializer, self).create(validated_data)


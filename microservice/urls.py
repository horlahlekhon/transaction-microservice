from django.urls import path

from microservice.views import TransactionsView

urlpatterns = [
    path('', TransactionsView.as_view(), name="create_transactions")
]
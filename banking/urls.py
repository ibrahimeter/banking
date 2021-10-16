from django.urls import path

from banking.views import create_account
from banking.views import my_accounts

urlpatterns = [
    path('create_account/',create_account),
    path('my_accounts/', my_accounts),
]
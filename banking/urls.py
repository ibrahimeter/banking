from django.urls import path

from banking.views import create_account
from banking.views import my_accounts
import banking.views as views


urlpatterns = [
    path('create_account/',create_account),
    path('my_accounts/', my_accounts),
    path('deposit/',views.deposit),
    path('transfer/', views.transfer),

]
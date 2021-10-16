from django.urls import path

from authentication.views import login
from authentication.views import test_authentication

urlpatterns = [
    path('login/',login),
    path('test_authentication/', test_authentication)]
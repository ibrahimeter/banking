import django.db
import json
import uuid
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from authentication.utils import is_authenticated
from .models import UserToken


# Create your views here.

@csrf_exempt
def login(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      username = data.get("username")
      password = data.get("password")
      user = authenticate(
         request, username=username, password=password)
      if user is not None:
         user_token = UserToken.objects.create(user=user, token=uuid.uuid4())
         return JsonResponse({"token": str(user_token.token)})
      else:
            # Wrong credentials
         return JsonResponse({"message": "Wrong credentials"})


def test_authentication(request):
    if not is_authenticated(request):
        return JsonResponse({"message": "You are not authenticated!"})
    return JsonResponse({"message": "You are authenticated!"})

    
     
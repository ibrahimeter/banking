from authentication.utils import is_authenticated
from django.shortcuts import render
from django.http import JsonResponse
from .models import BankAccount
from .models import serialize_bank_account
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def create_account(request):
    if not is_authenticated(request):
        return JsonResponse({"message": "you are not authenticated"})

    if request.method == "POST":
        bank_account = BankAccount.objects.create(user = request.user)
        return JsonResponse({"message":"success", "bank account":str(bank_account.bank_account)})

def my_accounts(request):
    if not is_authenticated(request):
        return JsonResponse({"message": "you are not authenticated"})

    list_my_accounts = []
    bank_accounts = BankAccount.objects.filter(user = request.user)
    for bank_account in bank_accounts:
        list_my_accounts.append(serialize_bank_account(bank_account))
    return JsonResponse({"my accounts":list_my_accounts})

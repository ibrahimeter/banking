from authentication.utils import is_authenticated
from django.shortcuts import render
from django.http import JsonResponse
from .models import serialize_bank_account
from .models import BankAccount
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def deposit(request):
    if not is_authenticated(request):
        return JsonResponse({"message": "you are not authenticated"})
    if request.method =="POST":
        data = json.loads(request.body)
        account = data.get("account")
        amount = data.get("amount")
        account_obj = BankAccount.objects.get(user= request.user, bank_account=account)
        account_obj.balance +=amount
        account_obj.save()
        return JsonResponse({"message":"success",
                            "account":serialize_bank_account(account_obj)
                            })  

@csrf_exempt
def transfer(request):
    if not is_authenticated(request):
        return JsonResponse({"message": "you are not authenticated"})
    if request.method == "POST":
        data = json.loads(request.body)
        src_account = data.get("src_account")
        dest_account= data.get("dest_account")
        amount = data.get("amount")
        src_account_obj = BankAccount.objects.get(user= request.user, bank_account=src_account)
        dest_account_obj = BankAccount.objects.get(bank_account= dest_account)
        try:
            src_account_obj.transfer(dest_account_obj, amount)
        except:
            return JsonResponse({"message":"you trying to send an amount that you do not have"})
        
        return JsonResponse({"message": "transfer success."})



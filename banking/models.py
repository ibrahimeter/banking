from django.db import models
from django.contrib.auth.models import User
import uuid

from django.http.response import JsonResponse



# Create your models here.
def serialize_bank_account(bank_account) -> dict:
    return {
        "bank_account": str(bank_account.bank_account),
        "balance": bank_account.balance
    }

class BankAccount(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    bank_account = models.UUIDField(default = uuid.uuid4())
    balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def transfer(self, dest_account, amount):
        if amount >self.balance:
            raise Exception("you trying to transfer an amount that you do not have ")
        
        self.balance -=amount
        dest_account.balance += amount
        self.save()
        dest_account.save()
        
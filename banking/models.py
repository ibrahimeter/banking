from django.db import models
from django.contrib.auth.models import User
import uuid


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
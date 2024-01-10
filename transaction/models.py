from django.db import models
from accounts.models import UserAccount

TRANSACTION_TYPE = (
    ('Deposite', 'Deposite'),
    ('Borrow', 'Borrow'),
    )
class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete = models.CASCADE)

    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    timestamp = models.DateTimeField(auto_now_add=True)



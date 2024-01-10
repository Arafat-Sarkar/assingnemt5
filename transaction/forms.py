from .models import Transaction
from django import forms

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount'
        ]
        
    # def save(self, commit=True):
    #     self.instance.account = self.account
    #     self.instance.balance_after_transaction = self.account.balance
    #     return super().save()


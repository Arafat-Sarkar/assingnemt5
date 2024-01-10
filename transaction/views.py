from django.shortcuts import render
from accounts.models import UserAccount
from django.views.generic import CreateView, ListView
from .models import Transaction
from django.urls import reverse_lazy
from .forms import DepositForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

class DepositeMoney(CreateView):
    model = Transaction
    form_class = DepositForm
    template_name = 'deposit.html'
    success_url = reverse_lazy('deposit') 

    def get_initial(self):
        initial = {'transaction_type': 'Deposite'}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        initial_balance = account.balance
        new_balance = initial_balance + amount
        
        transaction = form.save(commit=False)
        transaction.account = account
        transaction.transaction_type = 'Deposite'
        transaction.amount = amount
        transaction.balance_after_transaction = new_balance
        transaction.save()

        account.balance = new_balance
        account.save(update_fields=['balance'])
        
        return super().form_valid(form)
    

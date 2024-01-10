from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
from .models import UserAccount
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save() 

            UserAccount.objects.create(
                user = our_user,
            )
        return our_user
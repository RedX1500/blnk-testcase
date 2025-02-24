from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, LoanFund, Loan, LoanSettings
from django import forms



class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'role']

class Loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

class LoanFundform(forms.ModelForm):
    class Meta:
        model = LoanFund
        fields = ['amount',]

class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['fund', 'amount', 'term']

class LoanSettingsform(forms.ModelForm):
    class Meta:
        model = LoanSettings
        fields = ['min_amount', 'max_amount', 'interest_rate', 'duration']

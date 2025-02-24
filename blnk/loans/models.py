from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('loan_provider', 'Loan Provider'),
        ('loan_customer', 'Loan Customer'),
        ('bank_personnel', 'Bank Personnel'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# Loan Fund Model
class LoanFund(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'loan_provider'})
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Fund by {self.provider.username} - ${self.amount}"

# Loan Model
class Loan(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'loan_customer'})
    fund = models.ForeignKey(LoanFund, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    term = models.IntegerField()  # Number of months
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

# Bank Personnel Controls
class LoanSettings(models.Model):
    bank_personnel = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'bank_personnel'})
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField()  # In months
    




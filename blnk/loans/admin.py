from django.contrib import admin
from .models import LoanFund, Loan, LoanSettings, User

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email')
    list_filter = ('role',)
    search_fields = ('username', 'email')

# Register LoanFund
@admin.register(LoanFund)
class LoanFundAdmin(admin.ModelAdmin):
    list_display = ('provider', 'amount')
    search_fields = ('provider__username',)

# Register Loan
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'fund', 'amount', 'term', 'interest_rate', 'monthly_payment')
    list_filter = ('term', 'interest_rate')
    search_fields = ('customer__username', 'fund__provider__username')

# Register LoanSettings
@admin.register(LoanSettings)
class LoanSettingsAdmin(admin.ModelAdmin):
    list_display = ('min_amount', 'max_amount', 'interest_rate', 'duration', 'bank_personnel')
    search_fields = ('bank_personnel__username',)
    list_filter = ('interest_rate', 'duration')

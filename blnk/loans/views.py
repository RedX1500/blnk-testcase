from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserform, Loginform, LoanFundform, Loanform, LoanSettingsform
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserform()
    if request.method == "POST":
        form = CreateUserform(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('login')
    context = {'registerform':form}
    return render(request, 'register.html', context=context)

def loginpage(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = Loginform()
    context = {'loginform':form}
    return render(request, 'login.html', context=context)

def dashboard(request):
    return render(request, 'dashboard.html')

def loans(request):
    form = Loanform()
    if request.method == "POST":
        form = Loanform(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = request.user
            loan.save()
            return redirect('loans')
        else:
            form = Loanform()

    context = {'loanform':form}
    return render(request, 'loans.html', context=context)

# def loansettings(request):
#     settingsform = LoanSettingsform()
#     loanform = loanform()
#     if request.method == "POST":
#         settingsform = LoanSettingsform(request.POST)
#         loanform = loanform(request.POST)
#         if settingsform.is_valid() and loanform.is_valid():
#             loan_settings = settingsform.save(commit=False)
#             loan_form = loanform.save(commit=Fal)
#     return render(request, 'loansettings.html')

def loansettings(request):
    form = LoanSettingsform()
    if request.method == "POST":
        form = LoanSettingsform(request.POST)
        if form.is_valid():
            loan_settings = form.save(commit=False)
            loan_settings.bank_personnel = request.user
            loan_settings.save()
            return redirect('loansettings')
        else:
            form = LoanSettingsform()

    context = {'loansettingsform':form}
    return render(request, 'loansettings.html', context=context)


def loanfunds(request):
    form = LoanFundform()
    if request.method == "POST":
        form = LoanFundform(request.POST)
        if form.is_valid():
            loan_fund = form.save(commit=False)
            loan_fund.provider = request.user
            loan_fund.save()
            return redirect('loanfunds')
        else:
            form = LoanFundform()
            
    context = {'loanfundform':form}
    return render(request, 'loanfunds.html', context=context)

def logoutpage(request):
    logout(request)
    return redirect('/')
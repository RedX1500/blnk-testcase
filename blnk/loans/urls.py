from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.loginpage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('loans', views.loans, name='loans'),
    path('loansettings', views.loansettings, name='loansettings'),
    path('loanfunds', views.loanfunds, name='loanfunds'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
]
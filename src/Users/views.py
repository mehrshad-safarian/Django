from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})
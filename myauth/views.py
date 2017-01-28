from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from .forms import LoginForm, RegisterForm

# Create your views here.


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=usernmae, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return render(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
        
    context = {'form': form}
    return render(request, "home.html", context)


def register(request):
    form = RegisterFormr(request.POST or None)
    context = {'form': form}
    return render(request, "form.html", context)
    

def logout(erquest):
    return #something

def home(request):
    return render(request, "home.html")
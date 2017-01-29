from django.contrib.auth import authenticate 
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'myauth/userin.html')
                else:
                    return render(request, "Your account is disabled")
            else:
                print "invalid login details:{0}, {1}".format(username, password)
                return render(request, 'myauth/invalid.html',{},'Invalid login details')
    else:
        form = LoginForm()
        return render(request, 'myauth/form.html', {'form': form})


def register(request):
    form = RegisterFormr(request.POST or None)
    context = {'form': form}
    return render(request, "form.html", context)
    
@login_required
def user_logout(request):
    logout(request)
    return render(request, '',)

def home(request):
    user = User.objects.all()
    author = User.objects.get(username='maherrub')
    return render(request, 'myauth/home.html', {'user': user, 'author': author})
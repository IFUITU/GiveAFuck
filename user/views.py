from django.shortcuts import render, redirect
# from GiveAFuck.globals import crn
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Register(request):
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, '')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'You have registered successfully!')
            return redirect('main:index')         #("main:{}".format(crn))
        else:
            messages.warning(request, 'Form is not valid for registration! Try agan!')
    return redirect("main:index")
    # return render(request, 'pages/register.html', {"form":form})

def Login(request):
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Hello! & Welcome {}!'.format(request.user.username))
                return(redirect('main:index'))
            messages.error(request, 'Username or Passsword is not walid Try again!')
            form.add_error('username', 'Enter correct username or password')
    return redirect('main:index')
    # return render(request, 'pages/login.html',{'form':form})
@login_required
def Logout(request):
    if  request.user.is_authenticated:
        logout(request)
        messages.success(request,'Bye! See you again!')
    return redirect('main:index')
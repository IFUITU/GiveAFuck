from django.shortcuts import render, redirect
# from GiveAFuck.globals import crn
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def Register(request):
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, '')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main:index')         #("main:{}".format(crn))
        else:
            pass
    return redirect("main:index")

def Login(request):
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return(redirect('main:index'))

            form.add_error('username', 'Enter correct username or password')
    return render(request, 'includes/_login.html',{'form':form})

def Logout(request):
    if  request.user.is_authenticated:
        logout(request)
    return redirect('main:index')
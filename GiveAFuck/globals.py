from main.models import Category, Platform
from django.template.loader import render_to_string
from user.forms import RegisterForm,LoginForm
# from django.http import HttpResponse
def CATEGORY(request):
    category_query = Category.objects.all()
    return {
        'CATEGORY':category_query
    }

def Platforms(request):
    # platform = Game.objects.only('platform').all() returns games title
    platform = Platform.objects.all()
    return {'platforms':platform}

def crn(request):
    return {
        'crn':request.resolver_match.url_name,
    }


def register_modal(request):
    register_form = RegisterForm()
    login_form = LoginForm()
    return {
        "register_form":register_form,
        'login_form':login_form
    }
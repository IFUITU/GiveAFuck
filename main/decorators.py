from functools import wraps
from django.shortcuts import redirect

def login_required(funct):
    @wraps(funct)

    def g(request, *args, **kwargs):
        if request.user.is_authenticated:
            return funct(request, *args, **kwargs)
        else:
            return redirect('main:index')
    
    return g

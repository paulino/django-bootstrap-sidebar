from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

@login_required
def home(request):
    return render(request, 'home.html',{
        'sidebar_active': { 'home' : 'active' }
    })

@login_required
def popovers(request):
    return render(request, 'popovers.html',{
        'sidebar_active': {
            'popovers' : 'active',
            'examples' : 'true'
            }
    })


def raise_exception(request):
    raise Exception("This is an exception to show error 500 page")


def raise_403(request):
    raise PermissionDenied()



from django.http import HttpResponse
from django.shortcuts import redirect

from django.shortcuts import redirect

def wrapper_func(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  
        response = view_func(request, *args, **kwargs)
        if response is None:
            raise ValueError("View function returned None instead of an HttpResponse.")
        return response
    return _wrapped_view


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorised to view this page!')
        return wrapper_func
    return decorator

'''def admin_only(view_func):
    def wrapper_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Donor':
            return redirect('donor')
        if group == 'Finance':
            return redirect('finance')
        if group == 'Dataentry':
            return view_func(request, *args, **kwargs)        
    return wrapper_func
'''
    

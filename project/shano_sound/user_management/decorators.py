from functools import wraps
from django.shortcuts import render, redirect
from user_management.helpers import session_exists

def login_required(func):
    # @wraps
    def wrapper(*args, **kwargs):
        # import ipdb; ipdb.set_trace()
        req = args[0]
        print(req.session.get('email'))
        if session_exists(req):
            return func(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper

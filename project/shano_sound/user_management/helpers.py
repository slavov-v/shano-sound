def session_exists(request):
    if request.session.get('email', None):
        print(request.session['email'])
        return True
    return False

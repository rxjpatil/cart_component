from django.shortcuts import render
from django.shortcuts import render

def set_cookie_session(request):
    response = render(request, 'cookiesession/index.html')
    # Set a cookie
    response.set_cookie('cookie_name', 'cookie_value')
    # Set a session variable
    request.session['session_key'] = 'session_value'
    return response

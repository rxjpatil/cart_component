from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_cookie_session, name='set_cookie_session'),
]

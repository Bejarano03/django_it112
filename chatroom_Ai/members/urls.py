from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
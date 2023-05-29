from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('chat/', views.chat_view),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
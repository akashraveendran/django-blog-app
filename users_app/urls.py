from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]

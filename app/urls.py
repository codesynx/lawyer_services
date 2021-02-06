from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    # path('signin/', views.signin, name='signin'),
    # path('logout/', views.logout_request, name='logout'),
    # path('register/', views.register, name='register'),
    # path('about/', views.about, name='about'),
    # path('articles/', views.articles, name='articles'), 
]
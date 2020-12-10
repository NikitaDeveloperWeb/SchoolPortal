from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

#Маршрутизация
urlpatterns = [
    path('search/', views.user_search, name='user_search'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('news/', views.chat, name='news'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

]
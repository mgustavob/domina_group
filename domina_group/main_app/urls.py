from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    # path('user/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('user/<username>/subject/create/', views.SubjectCreate.as_view(), name='subject_create'),
    path('user/<username>/subject/index/', views.subject_index, name='subject_index'),
    path('user/<username>/subject/assoc_sub/<subject_id>', views.assoc_sub, name='assoc_sub'),
    path('user/<username>/subject/show/', views.subject_show, name='subject_show'),
    path('user/<username>/subject/<int:id>/delete/', views.SubjectDelete.as_view(), name='subject_delete'),

]

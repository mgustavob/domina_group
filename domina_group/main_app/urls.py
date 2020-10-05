from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('user/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('user/<username>/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<username>/subject/create/', views.SubjectCreate.as_view(), name='subject_create'),
    path('user/<username>/subject/index/', views.subject_index, name='subject_index'),
    path('user/<username>/subject/assoc_sub/<subject_id>', views.assoc_sub, name='assoc_sub'),
    path('user/<username>/subject/un_assoc_sub/<subject_id>', views.un_assoc_sub, name='un_assoc_sub'),
    path('user/<username>/subject/show/', views.subject_show, name='subject_show'),
    path('user/<username>/subject/<int:pk>/delete/', views.SubjectDelete.as_view(), name='subject_delete'),
    path('user/<user_id>/subject/<int:subject_id>', views.subject_detail, name='subject_detail'),
]

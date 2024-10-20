from django.contrib import admin
from django.urls import path,include
from .views import show_profile , CreateUserView , logout_user  , update_user
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('profile/', show_profile , name='profile'),
    path('', include('django.contrib.auth.urls')) ,
    path('signup', CreateUserView.as_view(), name='signup'),
    path('logout/', logout_user , name='test_logout'),
    #path('edit/<int:project_id>', edit, name='edit_product')
    path('update/', update_user, name='update_user'),

]


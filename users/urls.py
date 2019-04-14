from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UserCreate.as_view(), name="user_create"),
    path('activate/<str:token>/', views.UserActivate.as_view(), name="user_activate"),
    path('login/', views.UserLogin.as_view(), name="user_login"),
    path('forget_password/', views.UserForgetPassword.as_view(), name="user_forget_password"),
    path('forget_password/<str:token>/', views.UserForgetPasswordConfirm.as_view(), name="user_forget_password_confirm"),
]
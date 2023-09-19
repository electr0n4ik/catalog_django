from django.contrib.auth.views import LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import RegisterView, UserLoginView, UserProfileView, VerifyEmailView, PasswordResetView, \
    ConfirmPasswordResetView

app_name = UserConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', UserLoginView.as_view(template_name='user/user_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('verify_email/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('confirm_password_reset/<str:token>/', ConfirmPasswordResetView.as_view(), name='confirm_reset_password'),
]
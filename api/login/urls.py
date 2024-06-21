from django.urls import path
from .views import LoginView, ChangePasswordConfirmView, ForgetPasswordView, ResetPasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('change_password/<str:username>', ChangePasswordConfirmView.as_view(), name='change_password'),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]

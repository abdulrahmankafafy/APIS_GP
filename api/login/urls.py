from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('change_password/', PasswordResetConfirmView.as_view(), name='change_password'),
]

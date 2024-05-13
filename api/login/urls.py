from django.urls import path
from .views import LoginView, ChangePasswordConfirmView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('change_password/', ChangePasswordConfirmView.as_view(), name='change_password'),
]

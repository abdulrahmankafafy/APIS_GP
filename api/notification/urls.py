# notification/urls.py
from django.urls import path
from .views import NotificationListCreateView, NotificationDeleteView

urlpatterns = [
    path('users/<int:user_id>/notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('users/<int:user_id>/notifications/<int:notification_id>/', NotificationDeleteView.as_view(), name='notification-delete'),
]

from django.urls import path
from .views import NotificationListCreateView, NotificationDeleteView, NotificationListView

urlpatterns = [
    path('<int:user_id>/addNotification/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('<int:user_id>/deleteNotification/<int:notification_id>/', NotificationDeleteView.as_view(), name='notification-delete'),
    path('<int:user_id>/getNotifications/', NotificationListView.as_view(), name='notification-list'),
]

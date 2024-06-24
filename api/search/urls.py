from django.urls import path
from .views import SearchPostsView, SearchNotificationsView

urlpatterns = [
    path('searchPosts', SearchPostsView.as_view(), name='search-posts'),
    path('searchNotifications', SearchNotificationsView.as_view(), name='search-notifications'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.register.views import PersonViewSet, LogoutView, ProfileView

router = DefaultRouter()
router.register('register', PersonViewSet, basename='person')
app_name = 'register'

urlpatterns = [
    path('', include(router.urls)),
    path('verify_email/', PersonViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]
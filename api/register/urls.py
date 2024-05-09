from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.register.views import PersonViewSet

router = DefaultRouter()
router.register('register', PersonViewSet, basename='person')
app_name = 'register'

urlpatterns = [
    path('', include(router.urls)),
    path('verify-email/', PersonViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
]
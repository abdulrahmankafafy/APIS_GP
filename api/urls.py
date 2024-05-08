from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'register', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('verify-email/', PersonViewSet.as_view({'get': 'verify_email'}), name='verify_email'),
	path('api-auth/', include('rest_framework.urls'))
]

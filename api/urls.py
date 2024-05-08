from django.urls import path, include
# from .views import UserDetailAPI, RegisterUserAPIView
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'register', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]


from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('api.urls')),
  path('api/', include('api.posts.urls')),  
  path('api/', include('api.articles.urls')),  
]


from django.urls import path, include


urlpatterns = [
    path('', include('api.register.urls')),
    path('login/', include('api.login.urls')),
    path('posts/', include('api.posts.urls')),
]

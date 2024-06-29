from django.urls import include, path
from .views import UploadImageView


urlpatterns = [
    path('upload', UploadImageView.as_view(), name='upload_image'),
]

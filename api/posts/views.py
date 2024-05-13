from rest_framework import viewsets
from .models import post
from .serializers import PostSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# A function to ensure that users can only edit or delete their own posts
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100    

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from api.register.models import Person  # Assuming Person model is in the register app

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        try:
            author = Person.objects.get(username=username)
        except Person.DoesNotExist:
            raise serializer.ValidationError({"username": "User does not exist"})
        
        if author.account_type != 'Doctor':
            raise serializer.ValidationError({"username": "Only doctors can create articles"})
        
        serializer.save(author=author)

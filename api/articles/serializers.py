from rest_framework import serializers
from .models import Article
from api.register.models import Person  # Assuming Person model is in the register app

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ['id', 'author_name', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'author_name', 'created_at', 'updated_at']
    
    def get_author_name(self, obj):
        return obj.author.username

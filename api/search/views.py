from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Search
from .serializers import SearchSerializer
from api.posts.models import Question
from api.notification.models import Notification
from api.posts.serializers import QuestionSerializer
from api.notification.serializers import NotificationSerializer
from api.articles.models import Article
from api.articles.serializers import ArticleSerializer
from .models import Search
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchArticlesView(APIView):
    serializer_class = SearchSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            articles = Article.objects.filter(title__icontains=query)
            if articles.exists():
                # Serialize the articles to return them in the response
                article_serializer = ArticleSerializer(articles, many=True)
                return Response(article_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "No articles found with the given title."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SearchPostsView(APIView):
    serializer_class = SearchSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            questions = Question.objects.filter(title=query)
            if questions.exists():
                # Serialize the questions to return them in the response
                question_serializer = QuestionSerializer(questions, many=True)
                return Response(question_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "No questions found with the given title."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchNotificationsView(APIView):
    serializer_class = SearchSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            notifications = Notification.objects.filter(content__icontains=query)
            if notifications.exists():
                # Serialize the notifications to return them in the response
                notification_serializer = NotificationSerializer(notifications, many=True)
                return Response(notification_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "No notifications found containing the given content."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

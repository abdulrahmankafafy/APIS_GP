from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet, CommentViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

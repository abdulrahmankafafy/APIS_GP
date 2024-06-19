from rest_framework import serializers
from .models import Question, Answer, Comment, Vote

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'body', 'created_at', 'updated_at', 'accepted_answer']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'body', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'body', 'created_at', 'updated_at', 'question', 'answer']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'vote_type', 'question', 'answer']

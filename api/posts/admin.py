from django.contrib import admin

from .models import Question, Answer, Comment, Vote

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'title', 'body']
    list_display_links = ['id']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user_id', 'body']
    list_display_links = ['id']

admin.site.register(Answer, AnswerAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'body']
    list_display_links = ['id']

admin.site.register(Comment, CommentAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'vote_type']
    list_display_links = ['id']

admin.site.register(Vote, VoteAdmin)


from django.db import models
from api.register.models import Person 

class Question(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accepted_answer = models.OneToOneField('Answer', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

class Vote(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    vote_type = models.SmallIntegerField()  # +1 or -1
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)

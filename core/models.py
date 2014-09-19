from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    questionText = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    isAnswered = models.BooleanField(default=False)

    def __unicode__(self):
        return self.questionText

    #def get_absolute_url(self):
    #    return ("core.views.")


class Answer(models.Model):
    answerText = models.CharField(max_length=3000)
    question_id = models.ForeignKey(Question)
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.answerText

    #def get_absolute_url(self):






from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from core.models import Answer, Question

__author__ = 'emcee'

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answerText', 'question_id')
        widgets = {
            'question_id': HiddenInput()
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('questionText',)





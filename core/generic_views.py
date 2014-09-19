from django.views.generic.list import ListView
from core.forms import AnswerForm, QuestionForm
from core.models import Answer

__author__ = 'emcee'
from django.views.generic import DetailView

class QuestionDetailView(DetailView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question_id=self.object.pk).all()
        context['answerForm'] = AnswerForm(initial={'question_id':self.object.pk})

        return context

class QuestionListView(ListView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(QuestionListView, self).get_context_data(**kwargs)
        #context['answers'] = Answer.objects.filter(question_id=self.object.pk).all()
        context['questionForm'] = QuestionForm()

        return context
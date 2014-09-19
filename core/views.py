# Create your views here.
import  random
import logging
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from core.forms import QuestionForm, AnswerForm
from models import *

logger = logging.getLogger(__name__)

@login_required
def getRandomQuestion(request):
    question = Question.objects.filter(isAnswered=False).all()[:10]
    qLen = len(question)
    question = question[random.randint(0, qLen)]

    return HttpResponse(question)

@login_required
def postQuestion(request):
    if request.method != "POST":
        return HttpResponse("Must post.")
    elif not request.user.is_authenticated():
        return HttpResponse("not authenticated")

    question = Question()
    question.user = request.user
    questionForm = QuestionForm(request.POST, instance=question)
    questionForm.save()
    return HttpResponse("Question saved")

@login_required
def postAnswer(request):
    if request.method != "POST":
        return HttpResponse("Must post.")
    elif not request.user.is_authenticated():
        return HttpResponse("not authenticated")

    answer = Answer()
    answer.user = request.user
    answerForm = AnswerForm(request.POST, instance=answer)
    answerForm.save()
    return HttpResponse("answer saved")



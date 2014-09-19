from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
import authentication.urls

from core.generic_views import QuestionDetailView, QuestionListView
from core.models import Question
import core.views
import authentication.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AnswerMe.views.home', name='home'),
    # url(r'^AnswerMe/', include('AnswerMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',
        login_required(QuestionListView.as_view(
            queryset=Question.objects.all().order_by('-post_date')[:50],
            template_name='core/questions.html'
        )), name="list_questions" ),
    url(r'^postAnswer/$', core.views.postAnswer, name='postAnswer'),
    url(r'^postQuestion/$', core.views.postQuestion, name='postQuestion'),


    url(r'^getRandomQuestion/$', core.views.getRandomQuestion),
    url(r'^question/(?P<pk>\d+)/', login_required(QuestionDetailView.as_view(
        model=Question,
        template_name="core/questionDetail.html"
    )), name="question_detail"),
    #url(r'^accounts/login/$', authentication.views.login, name="login"),
    #url(r'^accounts/login/$', authentication.views.login, name='login'),
    url(r'^accounts/', include(authentication.urls)),


)

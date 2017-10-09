from django.conf.urls import url
from .views import question, choice, vote, _login, main
urlpatterns = [
    url(r'^vote/question/$',question,name="question"),
    url(r'^vote/choice/(?P<id>\w+)/$',choice,name="choice"),
    url(r'^vote/vote/(?P<id>\w+)$',vote,name="vote"),
    url(r'^vote/_login/$', _login, name="_login"),
    url(r'^vote/main/$', main, name="main")
]
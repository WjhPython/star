from django.conf.urls import url
from .views import question, choice, vote, login
urlpatterns = [
    url(r'^vote/question/$',question,name="question"),
    url(r'^vote/choice/(?P<id>\w+)/$',choice,name="choice"),
    url(r'^vote/vote/(?P<id>\w+)$',vote,name="vote"),
    url(r'^login/', login, name="login")
]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render, render_to_response

from models import Question, Choice
from models import User

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    if not (username or password):
        Error = "用户名或者密码错误！"
        context = ("login.html",{"Error", Error})
        return render_to_response(context)


def vote(request, id):
    if request.method == "post":
        id = request.POST[id]
        print(id)
    cho = Choice.objects.filter(id=id).first()
    votes = cho.votes+1
    Choice.objects.filter(id=id).update(votes=votes)
    question = Question.objects.filter(id=cho.question.id)
    choices = Choice.objects.filter(question=question).all()
    return render_to_response('choice.html',{'choices': choices})


def choice(request, id):
    question = Question.objects.filter(id=id)
    choices = Choice.objects.filter(question=question).all()
    return render_to_response('choice.html',{'choices': choices})


def question(request):
    questions = Question.objects.all()
    return render_to_response('question.html',{'questions': questions})
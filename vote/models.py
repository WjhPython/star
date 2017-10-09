# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models
# Create your models here.


class Banana(models.Model):
    title = models.CharField(max_length=300, unique=True, db_index=True, blank=False)
    url = models.CharField(max_length=300,db_index=True,blank=False)
    picture = models.ImageField(blank=True, default="")
    movie_time = models.CharField(max_length=100, blank=True, default="")
    add_date = models.DateTimeField()

    class Meta:
        db_table = "banana"


class User(models.Model):
    username = models.CharField(max_length=15, unique=True, db_index=True)
    password = models.CharField(max_length=50)
    last_login_date = models.DateTimeField()
    register_date = models.DateTimeField()

    class Meta:
        db_table = "user"


class Question(models.Model):
    """
        字段：
        question: 投票的问题
        date: 发起投票的时间
    """
    question = models.TextField(default="")
    date = models.DateTimeField()


    class Meta:
        db_table = "question"


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = "choice"


class UserVote(models.Model):
    user_id = models.IntegerField()
    choice_id = models.IntegerField()
    question_id = models.IntegerField()

    class Meta:
        index_together = ["user_id",
                          "choice_id",
                          "question_id"]


class UserDiviceId(models.Model):
    diviced_id = models.CharField(max_length=100,blank=True,default="")
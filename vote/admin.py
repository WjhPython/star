# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from models import Question
from models import Choice
from models import UserDiviceId
from models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "register_date", "last_login_date")
    list_filter = ("register_date",)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice","votes")



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['question']}),
                ('时间', {'fields': ['date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]
    list_display = ('question', 'date')


class UserDiviceIdForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             queryset=Choice.objects.all())

    class Meta:
        model = UserDiviceId
        fields =["diviced_id"]

class UserDiviceIdAdmin(admin.ModelAdmin):
    form = UserDiviceIdForm
    list_display = ("diviced_id",)

admin.site.register(User, UserAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserDiviceId, UserDiviceIdAdmin)
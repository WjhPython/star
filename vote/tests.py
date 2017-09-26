# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from .views import add
# Create your tests here.

class AddCaseTest(TestCase):

    def setUp(self):
        c = Client()
        response = c.post('vote/add/')

    def testadd(self):
        self.assertEquals(add, "nihao")
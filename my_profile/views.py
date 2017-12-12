# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import *

response = {}
def index(request):
    response['author'] = 'jojo'
    html = 'my_profile/myNew.html'
    return render(request, html, response)
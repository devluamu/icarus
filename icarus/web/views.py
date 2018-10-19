# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.core.urlresolvers import reverse

def index(request):
    template = loader.get_template('web/anime-index.html')
    return render(request, 'web/anime-index.html')

# Create your views here.

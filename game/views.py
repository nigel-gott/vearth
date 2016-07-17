from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from game.models import Human


def index(request):
    template = loader.get_template('game/index.html')
    rendered = template.render({'content': str(Human.objects.all())}, request)
    return HttpResponse(rendered)
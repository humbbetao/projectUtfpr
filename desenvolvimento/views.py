# Create your views here.

from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms

from desenvolvimento.models import Curso, Funcionario
from models import Professor


def index(request):

    return render_to_response('index.html', {})

def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,
    })
    return HttpResponse(t.render(c))


def professor(request):
    listasdeFunc = Funcionario.objects.all().order_by('nome')

    t = loader.get_template('professor.html')
    c = RequestContext(request, {
        'listasdeProf': listasdeFunc,
    })
    return HttpResponse(t.render(c))
    #return render_to_response('professor.html', {})


def eventos(request):
    return render_to_response('eventos.html', {})


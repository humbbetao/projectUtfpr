# Create your views here.

from django.template import Context, loader
from desenvolvimento.models import Curso, Professor
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
def index(request):  
    latest_curso_list = Curso.objects.order_by('-nome')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_curso_list': latest_curso_list,
    })
    return HttpResponse(template.render(context))



def cursos(request):
   listaDeCurso = Curso.objects.all().order_by('-nome')
   t = loader.get_template('curso.html')
   c = RequestContext(request, {
	'listaDeCurso': listaDeCurso,
   })
   return HttpResponse(t.render(c))


def professores(request):
    listaDeProfessores = Professor.objects.all().order_by('-nome')
    t = loader.get_template('professor.html')
    c = RequestContext(request, {
      'listaDeProfessores': listaDeProfessores,
    })
    return HttpResponse(t.render(c))

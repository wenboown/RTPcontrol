# Create your views here.

# 1 main panel, show current T + plot + pressure (send alert email if it doesn't work), current recipe, select recipe, import button, export button, create recipe button
# 2 create recipe view
# 3 popup select recipe view

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from Tcontrol.models import Recipe, Logs
from Tcontrol.forms import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.forms.models import modelformset_factory

def main_panel(request):
    recipes=Recipe.objects.all()
    RecipeSet=modelformset_factory(Recipe,extra=7,max_num=8)
    n=RecipeSet(queryset=Recipe.objects.all().order_by('step'))
    c={'recipes':n}
    c.update(csrf(request))
    return render_to_response('main_panel.html', c)

def add(request):
    return HttpResponse("test add")

def run(request):
    RecipeSet = modelformset_factory(Recipe, extra=7, max_num=8)
    if request.method == 'POST':
        formset=RecipeSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse("post result")
        else:
            return HttpResponse("something was wrong with the input")

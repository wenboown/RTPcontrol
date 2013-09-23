# Create your views here.

# 1 main panel, upload and save recipes and etc.
# 2 Run panel, display data plot and status
# 3 popups

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from Tcontrol.models import Recipe, Logs
from Tcontrol.CN8201 import CN8201
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.forms.models import modelformset_factory

def main_panel(request):
    RecipeSet=modelformset_factory(Recipe,extra=7,max_num=8)
    n=RecipeSet(queryset=Recipe.objects.all().order_by('step'))
    c={'recipes':n}
    c.update(csrf(request))
    return render_to_response('main_panel.html', c)

def run(request):
    RecipeSet = modelformset_factory(Recipe, extra=7, max_num=8)
    if request.method == 'POST':
        formset=RecipeSet(request.POST)
        if formset.is_valid():
            formset.save()
            device=CN8201("com6")
            return HttpResponse("post result")
        else:
            return HttpResponse("something was wrong with the input")

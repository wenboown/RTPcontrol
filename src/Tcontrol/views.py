# Create your views here.

# 1 main panel, show current T + plot + pressure (send alert email if it doesn't work), current recipe, select recipe, import button, export button, create recipe button
# 2 create recipe view
# 3 popup select recipe view

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from Tcontrol.models import Recipe, Logs

def main_panel(request):
    # r=Recipe.objects.all()
    # if r.fetchone():
    #     pass
    # else:
    #     k=Recipe()
    #     r=[k]
    k = Recipe()
    r=[k]

    c={'recipe':r}
    c.update(csrf(request))
    return render_to_response('main_panel.html', c)

def add(request):
    return HttpResponse("test add")

# Create your views here.

# 1 main panel, upload and save recipes and etc.
# 2 Run panel, display data plot and status
# 3 popups

import os, json, datetime, csv
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from Tcontrol.models import Recipe, Logs
from Tcontrol.CN8200Ctrl import CN8201
#from dajax.core import Dajax
#from dajaxice.decorators import dajaxice_register
from django.forms.models import modelformset_factory, fields_for_model
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

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
            f=formset.save()
            device=CN8201("com9")
            for line in formset.cleaned_data:
                if len(line)!=0:
                    device.write("%02d"%(41+line['step']),"%+07.4f"%line['ramp_time'])
                    device.write("%02d"%(57+line['step']),"%+07.4f"%line['soak_level'])
                    device.write("%02d"%(65+line['step']),"%+07.4f"%line['soak_time'])
                else:
                    break
            device.write("06","+5.0000")
            return HttpResponse("post result")
        else:
            return HttpResponse("something was wrong with the input")
'''
def save_recipe(request):
    myfile = StringIO()
    writer = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_headings = ['UHVRTP V1.0 recipe. Timestamp: '+str(datetime.datetime.today())]
    csv_fields = fields_for_model(Recipe).keys()
    csv_data=[]
    writer.writerow(csv_headings)
    writer.writerow(csv_fields)
    row_number = 0
    while row_number < 8:
        data = model_to_dict(Recipe)
        csv_data += [data[field] for field in fields]
        writer.writerow(csv_data)
        row_number+=1
    file_content = myfile.getvalue()
    myfile.close()
    response = HttpResponse(file_content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=assumption_{}.csv'.format(assumption_id)
    return response

def user_log(request):
   log_field=fields_for_model(Logs)
'''
def standby(request):
    device=CN8201("com9")
    if device.write("06","+2.0000") == '0':
        return HttpResponse("standby succeed")
    else:
        return HttpResponse("standby error")

def operate(request):
    device=CN8201("com9")
    if device.write("06","+3.0000") == '0':
        return HttpResponse("normal operate succeed")
    else:
        return HttpResponse("normal operate error")


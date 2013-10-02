import os
from django import forms
from django.forms import ModelForm, Textarea, DateTimeInput,TextInput
from Tcontrol.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.widgets import DateInput, HiddenInput


class LogForm(ModelForm):
    class Meta:
        model = Logs
        fields = ('time_stamp', 'user', 'note')
        widgets = {
            'time_stamp': DateTimeInput(attrs={'class': "text ui-widget-content ui-corner-all"}),
            'user': TextInput(attrs={'class': "text ui-widget-content ui-corner-all"}),
            'note': Textarea(attrs={'rows': 3, 'class': "text ui-widget-content ui-corner-all"}),
        }

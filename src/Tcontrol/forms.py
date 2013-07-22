import os
from django import forms
from django.forms import ModelForm, Textarea
from Tcontrol.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.widgets import DateInput, HiddenInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
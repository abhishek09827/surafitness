from dataclasses import field, fields
from operator import mod
from socket import fromshare
from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogForms(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields =['content']
__author__ = 'root'

from django import forms
from django.forms import widgets, ModelForm
from .models import *
# from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

import logging
logger = logging.getLogger(__name__)

class FileIUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))
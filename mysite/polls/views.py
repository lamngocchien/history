# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import logging
import json
logger = logging.getLogger(__name__)
from django.http import HttpResponse
from utils.filter import custom_login_required, get_templates_path
from polls.models import *
from polls.forms import *
from django.shortcuts import render


def load_page(request, page_name):
    page = 'templates/sb-admin/pages/%s.html' % page_name
    page = get_templates_path(page)
    logger.debug(page)
    return render(request, page)

# @custom_login_required
def index(request):
    logger.debug("=================LOGIN=OK=================")
    # return HttpResponse("Hello, world. You're at the polls index.")
    page = get_templates_path('templates/sb-admin/base.html')
    # logger.debug(page)
    return render(request, page, {})

# @custom_login_required
def home(request):
    data = Choice()._get_data(choice_text__in=['Bad','Good'])
    for i in data:
        logger.debug(i)
    data1 = Choice()._get_data(input_data=data,choice_text__in=['Bad'])
    for i in data1:
        logger.debug("==%s==",i)
    Choice()._update_data(input_data=data1,choice_text='Very Bad')

    return HttpResponse("Hello, world. You're at the polls Home.")

# @custom_login_required
def demo(request,pk,id):
    logger.debug('PK: %s ID: %s',pk,id)
    return HttpResponse("Hello, world. You're at the polls Home. PK:"+str(pk)+" ID:"+str(id))

def highchart_api(request):
    data = [{
        'name': 'Year 1800',
        'data': [107, 31, 635, 203, 2]
    }, {
        'name': 'Year 1900',
        'data': [133, 156, 947, 408, 6]
    }, {
        'name': 'Year 2012',
        'data': [1052, 954, 4250, 740, 38],
        'marker': {'fillColor': '#BF0B23', 'radius': 10},
        'url': "{% url 'polls:home' %}",
    }]
    cata = ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
    response_data = [data,cata]
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def highchart(request):
    # return HttpResponse("Highchart Demo")

    # page = "C:/Python27/Scripts/mysite/templates/polls/highchart.html"
    page = get_templates_path('templates/polls/highchart.html')
    # logger.debug(page)
    return render(request, page, {})


# fp = open(unicode(path2, "utf-8"))

def file_upload(request):

    if request.method == 'POST':
        logger.debug("request.POST: %s",request.POST)
        form = FileIUploadForm(request.POST)
        logger.debug(form)
        file = request.FILES['file']
        logger.debug("file: %s",file)
        path = file.temporary_file_path
        logger.debug("path: %s", path)
        # logger.debug(abc)
    # page = 'sb-admin/pages/mypages/%s.html' % page_name
    page = get_templates_path('templates/sb-admin/pages/file_upload.html')
    logger.debug(page)
    form = FileIUploadForm()

    return render(request, page, {'form': form})
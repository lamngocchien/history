__author__ = 'root'
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib import messages
from django.shortcuts import render
from utils.filter import login_success, get_templates_path
from django.utils.translation import gettext as _
import logging
from django.contrib.auth.models import User as OriginalUser
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


# Load login page
@login_success
def load_login_page(request):
    # path = get_templates_path()
    # BASE_DIR = os.path.dirname()
    # import os
    # import json
    # config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..', '..', 'config', 'config.json'))
    # print config_file_path
    # try:
    #     with open(config_file_path) as data_file:
    #         data = json.load(data_file)
    #         django_app_data = data["application"]
    #         project_dir_name = django_app_data["project_dir_name"]
    # except:
    #     logger.debug("Could not found config.json file")
    # path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..', project_dir_name))
    # print 'temp', path
    # path = path.replace('\\', '/')+'/'
    # print 'temp:', path
    #
    # # logger.debug("Path: %s",path)
    # logger.debug('go to load login page')
    # logger.debug(request.GET.get('next', '/'))
    # page = path + "templates/polls/login.html"
    # # page = "templates/polls/login.html"
    # # page = 'D:/django2exe-dist/django2exe-dist/mysite/templates/polls/login.html'
    page = get_templates_path('templates/polls/login.html')
    logger.debug(page)
    return render(request, page, {'next': request.GET.get('next', '/')})


@login_success
def login(request):
    logger.debug("====GO====TO====LOGIN====")
    # Can't get parameter
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError as ex:
        logger.warning(ex)
        return load_login_page(request)

    # Get next url when sucess login if next url is exist
    next_url = request.GET.get('next', '/')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            logger.debug("LOGIN SUCCESSFULL")
            return HttpResponseRedirect(next_url)
        else:
            logger.debug('do not active account')
            messages.error(request, _('User do not active'))
            return load_login_page(request)
    else:
        logger.debug('invalid account')
        messages.error(request, _('Please check username or password'))
        return load_login_page(request)

    logger.debug('go to sb_admin')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('polls:login_page'))

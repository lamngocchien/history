__author__ = 'root'

import logging
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)


def custom_login_required(f):
    def wrap(request, *args, **kwargs):
        # logger.debug("Request: %s",request)
        logger.debug('Filter login')
        logger.debug(request.user.is_authenticated())
        if not request.user.is_authenticated():
            # return redirect(reverse('sb_admin:load_my_page', args=('login', )))
            logger.debug("Redirect to login page")
            logger.debug('request.path = %s',request.path)
            return redirect('%s?next=%s' % (reverse('polls:login_page'), request.path))
        return f(request, *args, **kwargs)
        wrap.__doc__ = f.__doc__
        wrap.__name__ = f.__name__
    return wrap


# Filter for successful login. If successful login, can't go to login page
def login_success(f):
    def wrap(request, *args, **kwargs):
        logger.debug('Filter success login')
        if request.user.is_authenticated():
            logger.debug('=======user: %s', request.user.username)
            return HttpResponseRedirect(reverse('polls:polls'))
        else:
            logger.debug('NOK=======user: %s', request.user.username)
        return f(request, *args, **kwargs)
        wrap.__doc__ = f.__doc__
        wrap.__name__ = f.__name__
    return wrap




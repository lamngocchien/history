"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin

# class AccessUser:
#     has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True
#
# admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

from polls import  views
urlpatterns = [
    url(r'^core/', include('polls.urls', namespace='polls')),
    url(r'^', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home,),
]

from django.conf import settings
import os
if settings.DEBUG404:
    urlpatterns += \
        patterns(
            '',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': os.path.join(os.path.dirname(__file__),'..', 'static')}),
        )
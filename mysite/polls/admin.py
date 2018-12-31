# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Unauth
from django.contrib.auth.models import User, Group


# We add this so no authentication is needed when entering the admin site
class AccessUser(object):
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True

admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

# We add this to remove the user/group admin in the admin site as there is no user authentication
admin.site.unregister(User)
admin.site.unregister(Group)

# Create superuser for admin use in case it doesn't exist
try:
    User.objects.get_by_natural_key('admin')
except User.DoesNotExist:
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

# Unauth



# Register your models here.
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
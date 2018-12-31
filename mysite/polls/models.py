# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
import logging
logger = logging.getLogger(__name__)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):  # __unicode__ on Python 2
        return self.question_text


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _get_data(self,input_data=None, case=None, **kwargs):
        # if kwargs is not None:
        #     for key, value in kwargs.iteritems():
        #         print "%s == %s" % (key, value)
        if input_data:
            data = input_data.filter(**kwargs)
        else:
            data = Choice.objects.filter(**kwargs)
        if case:
            logger.debug("CASE is %s",case)
        return data

    def _update_data(self,input_data=None, **kwargs):
        if input_data:
            data = input_data.update(**kwargs)
        else:
            data = Choice.objects.update(**kwargs)

    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninja(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")




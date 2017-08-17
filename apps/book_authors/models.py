# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):

    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
class Author(models.Model):
        fname = models.CharField(max_length=255)
        lname = models.CharField(max_length=255)
        email = models.CharField(max_length=255)
        note = models.TextField(1000, null=True)
        created_at= models.DateTimeField(auto_now_add=True)
        updated_at= models.DateTimeField(auto_now=True)
        books= models.ManyToManyField(Book, related_name="authors")
        



from django.db import models
#from django.conf import settings
#from django.contrib.auth.models import User
from datetime import datetime
import re
import os

def product_image_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'product/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products",null = True, blank = True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = product_image_directory_path, blank = True, null = True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

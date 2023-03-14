from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os

def get_image(request,image_name):
    try:
        image=storage.child(image_name).download(None)

        return HttpResponse(image,content_type='image.jpeg')
    except:
        return HttpResponse(status=404)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import requests
from .models import Userdetail
import json
import sqlite3
def maps(request):
	drivers = Userdetail.objects.all()
	message_me = Userdetail.objects.all().count()
	return render( request , "dashboard.html",{ "dridetail" : drivers, "number" : message_me})
		#return render( request , "tushar.html" , {"cursor" : cursor })
# Create your views here.
def index(request):
    return render(request, "index.html",{})

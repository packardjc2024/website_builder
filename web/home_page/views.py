from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import requests
from datetime import datetime, time, timedelta


###############################################################################
# Functions
###############################################################################



###############################################################################
# Views
###############################################################################

def index(request):
    context = {}

    return render(request, 'home_page/index.html', context)
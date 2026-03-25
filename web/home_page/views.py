from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
from django.conf import settings


###############################################################################
# Views
###############################################################################

def index(request):
    context = {}
    return render(request, 'home_page/index.html', context)
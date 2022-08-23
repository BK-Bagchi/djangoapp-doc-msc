from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("1st view of the polls app created")

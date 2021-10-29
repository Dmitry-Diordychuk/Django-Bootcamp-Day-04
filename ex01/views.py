from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def django(request):
    template = loader.get_template("ex01/django.html")
    context = {}
    return HttpResponse(template.render(context, request))


def display(request):
    template = loader.get_template("ex01/display.html")
    context = {}
    return HttpResponse(template.render(context, request))


def templates(request):
    template = loader.get_template("ex01/templates.html")
    context = {}
    return HttpResponse(template.render(context, request))
